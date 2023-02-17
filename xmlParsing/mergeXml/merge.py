import os, os.path, sys
import glob
from xml.etree import ElementTree

def run(files):
    xml_files = glob.glob(files +"/*.xml")
    xml_element_tree = None
    for xml_file in xml_files:
        data = ElementTree.parse(xml_file).getroot()
        # print(ElementTree.tostring(data))
        # print(data.iter('results')) 포인터같은 거인듯?
        for result in data.iter('results'): #xml의 파싱의 getroot의 "results" 태그를 뽑는다.
            if xml_element_tree == None:
                xml_element_tree = data
                insertion_point = xml_element_tree.findall("./results")[0]
            else:
                insertion_point.extend(result)
    if xml_element_tree is not None:
        text_file = open("mergeCom.xml", "w")
        text_file.write(ElementTree.tostring(xml_element_tree).decode())
        text_file.close()
run('mergeXml')