import urllib.request
import requests
from bs4 import BeautifulSoup
import csv

headers={
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


url="https://www.thepaper.cn/newsDetail_forward_1247549"
response=requests.get(url,headers=headers)
data=response.text
soup=BeautifulSoup(data,"html.parser")
Each_Title=soup.select("body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > h1")
Each_Title=Each_Title[0]
Each_Title=Each_Title.get_text()
# print(Each_Title)

Each_Content=soup.select("body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > div.news_txt")
Each_Content=Each_Content[0]
Each_Content=Each_Content.get_text().replace("(本文来自澎湃新闻，更多原创资讯请下载“澎湃新闻”APP)","").replace("\n","").replace(" ","").replace(u"\xa0","")
print(Each_Content)

