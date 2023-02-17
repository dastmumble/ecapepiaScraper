import requests
from bs4 import BeautifulSoup


url = 'http://data.ekape.or.kr/openapi-data/service/user/grade/auct/pigPriceDetail'
params ={'serviceKey' : 'nuRQIAuQHVRpf6FIS7ROERFaRprJYUefG8H65yAeZlgd5i1d0n3kN9EmbsYx438A31YhDPY+kzT7Orx5TjA5GA==', 'abattCd' : '0302', 'startYmd' : '20160101', 'endYmd' : '20160131', 'skinYn' : 'N', 'sexCd' : '025001' }

#soup 오브젝트 생성
response = requests.get(url, params=params)
xml_data = response.text
soup = BeautifulSoup(xml_data, "xml")

#필요없는 태그 지우기
removeTags = soup.findAll(["header","judgeSexNm","notice","gradeCd","gradeType","gradeType","judgeSexCd","skinNm","skinYn"])
for removeTag in removeTags:
    removeTag.extract()

#result.xml로 쓰기
with open("result.xml", "w", encoding="utf-8") as f:
    f.write(str(soup.prettify()))


