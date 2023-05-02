import xml.etree.ElementTree as ET
import os

xml_path = './xmlParsing/parseXml/example.xml'
xml_file = open(xml_path, 'rt', encoding='UTF8') #xml 파일 열기

anno = ET.parse(xml_file)
pig_detail = anno.getroot()

items = pig_detail.findall('.//item')
for item in items:
    attribute = item.find('gradeNm').tag
    print(attribute)