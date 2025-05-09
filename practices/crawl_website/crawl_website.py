import pandas as pd

from pathlib import Path
import requests
from bs4 import BeautifulSoup
import xlsxwriter as xlsx
import time

ROOTDIR = Path(__file__).parent

class Skill:
    def __init__(self, id, champId, skillName, description, linkImage, order):
        self.id = id
        self.champId = champId
        self.skillName = skillName
        self.description = description
        self.linkImage = linkImage
        self.order = order
        
    def printToConsole(self):
        print(self.id)
        
skills = []

def writeExcel(skillItem, worksheet, rowIndex):
    columnIndex = 0
    for attr, value in skillItem.__dict__.items():
        print(f"row= {rowIndex}")
        print(f"col= {columnIndex}")
        worksheet.write(rowIndex, columnIndex, value)
        columnIndex += 1
    # row index
    # loop list
        # column index
        # intrate property
        # write
    # close
    print("Done")


def run():
    try:
        response = requests.get("https://lienquan.garena.vn/hoc-vien/tuong-skin/")
        wb = xlsx.Workbook(f"{ROOTDIR}/output.xlsx")
        worksheet = wb.add_worksheet()
        rowIndex = 1
        # write header text
        worksheet.write("A1", "id")
        worksheet.write("B1", "champId")
        worksheet.write("C1", "skillName")
        worksheet.write("D1", "description")
        worksheet.write("E1", "linkImage")
        worksheet.write("F1", "order")
        
        if response.status_code == 200:
            htmlValue = response.text
            soup = BeautifulSoup(htmlValue, 'html.parser')
            
            for item in soup.find_all("a", "st-heroes__item"):
                link = item.get("href")
                champId = Path(link).name
                response2 = requests.get(f"{link}")
                
                if response2.status_code == 200:
                    htmlValue2 = response2.text
                    soup2 = BeautifulSoup(htmlValue2, 'html.parser')
                    index = 1
                    for item in soup2.find("ul", "hero__skills--list").find_all("a"):
                        skillId = item.get("href").replace("#", "")
                        print(champId)
                        
                        skillName = item.get("title")
                        linkImage = item.find("img").get("src")
                        description =  soup2.find("div", id=skillId).find("article").get_text()
                        item = Skill(len(skills) + 1,
                                            champId=champId,
                                            skillName=skillName,
                                            description=description,
                                            linkImage=linkImage,
                                            order=index)
                        skills.append(item)
                        index += 1
                        writeExcel(item, worksheet, rowIndex)
                        rowIndex += 1
                time.sleep(3)
    finally:
        wb.close()
run()