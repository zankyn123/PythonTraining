import pandas as pd

from pathlib import Path
import requests
from bs4 import BeautifulSoup

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


def run():
    response = requests.get("https://lienquan.garena.vn/hoc-vien/tuong-skin/")
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
                    linkImage = item.get("src")
                    description =  soup2.find("div", id=skillId).find("article").get_text()
                    skills.append(Skill(len(skills) + 1,
                                        champId=champId,
                                        skillName=skillName,
                                        description=description,
                                        linkImage=linkImage,
                                        order=index))
                    index += 1
    
run()

import xlsxwriter as xlsx
def writeExcel(arrays: list):
    wb = xlsx.Workbook("")