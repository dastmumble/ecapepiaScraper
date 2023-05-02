import xml.etree.cElementTree as ET
import datetime
import requests
from bs4 import BeautifulSoup


url = 'http://data.ekape.or.kr/openapi-data/service/user/grade/auct/pigPriceDetail'
params ={
    'serviceKey' : 'nuRQIAuQHVRpf6FIS7ROERFaRprJYUefG8H65yAeZlgd5i1d0n3kN9EmbsYx438A31YhDPY+kzT7Orx5TjA5GA==',
    'abattCd' : '057016', #전국(제주제외)
    'startYmd' : input('시작기간(YYYYMMDD) : '),
    'endYmd' : input('종료기간(YYYYMMDD) : '), 
    'skinYn' : 'Y', # 탕박
    'sexCd' : '' } # 전체 성별

#soup 오브젝트 생성
response = requests.get(url, params=params)
xml_data = response.text
soup = BeautifulSoup(xml_data, "xml")


#필요없는 태그 지우기
removeTags = soup.findAll(["header","judgeSexNm","notice","gradeCd","gradeType","gradeType","judgeSexCd","skinNm","skinYn"])
for removeTag in removeTags:
    removeTag.extract()

#schema 참조
response = soup.find('response')
response['xmlns:xsi'] = "http://www.w3.org/2001/XMLSchema-instance"

#xml item 순서바꾸기
old_items = soup.findAll('item')
for old_item in old_items:
    new_item = soup.new_tag('item')
    new_item.append(old_item.startYmd)
    new_item.append(old_item.endYmd)
    new_item.append(old_item.gradeNm)
    new_item.append(old_item.auctCnt)
    new_item.append(old_item.weight)
    new_item.append(old_item.auctAmt)
    new_item.append(old_item.maxAuctAmt)
    new_item.append(old_item.minAuctAmt)
    new_item.append(old_item.sumAuctAmt)
    new_item.append(old_item.sumWeight)
    old_item.replace_with(new_item)

#result.xml로 쓰기
today = datetime.date.today
with open(f"./result/{params['startYmd'][-4:]}~{params['endYmd'][-4:]}_돼지경락상세.xml", "w", encoding="utf-8") as f:
    f.write(soup.prettify())




