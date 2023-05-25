#xml -> xslx를 위한 파싱
from bs4 import BeautifulSoup
with open("./result/0213~0217_돼지경락상세.xml", encoding="UTF-8") as input:
    soup = BeautifulSoup(input, 'xml')
    items = soup.find_all("item")
    print(items)




#지난주 월~금 날짜 출력
# import datetime
# from dateutil.relativedelta import *

# #지난주 월요일과 금요일을 YYYYMMDD로 출력함.
# monday = datetime.date.today() + relativedelta(weekday=MO(-2))
# monday = monday.strftime('%Y%m%d')

# friday = datetime.date.today() + relativedelta(weekday=FR(-1))
# friday = friday.strftime('%Y%m%d')
# print(monday,friday)



