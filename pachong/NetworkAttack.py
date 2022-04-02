import urllib.request
import requests
from bs4 import BeautifulSoup
import csv
import re


headers={
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"
}

title_jump_list=[]
year_list=[]



with open("C:/Users/OK/Desktop/知识图谱_任务/2网络攻击事件（2014-2017）/pengpai_attack.html","r",encoding="utf-8") as f:
    content=f.read()
    # print(content)
    soup=BeautifulSoup(content,"html.parser")
    for i in range(1,37):
        # Title = soup.select("#tbody > tr:nth-child(" + str(i) + ") > td:nth-child(1) > a > span > b")
        #                        mainContent > div:nth-child(1) > h2 > a
        #                        mainContent > div:nth-child(245) > h2 > a
        #                        mainContent > div:nth-child(37) > h2 > a
        #                        mainContent > div:nth-child(1) > div > span//没有评论
        #                        mainContent > div:nth-child(3) > div > span:nth-child(2)//有评论
        #                        mainContent > div:nth-child(6) > div > span:nth-child(2)
        #                        mainContent > div:nth-child(5) > div > span.trbszan
        Title=soup.select("#mainContent > div:nth-child("+str(i)+") > h2 > a")
        if Title:
            Title=Title[0]
            Title=Title["href"].replace("\n","").replace(" ","")
        else:
            continue

        Year=soup.select("#mainContent > div:nth-child("+str(i)+") > div > span:nth-child(1)")
        Year=Year[0]
        Year=Year.get_text()
        if Year:
            Year=re.match(r'\d{4}-\d{2}-\d{2}',Year)
            if Year and (Year is not None):
                Year = Year.group()
            else:
                Year = soup.select("#mainContent > div:nth-child(" + str(i) + ") > div > span:nth-child(2)")
                Year = Year[0]
                Year = Year.get_text()
        else:
            continue



        title_jump_list.append(Title)
        Year=re.match(r"\d{4}",Year).group()
        year_list.append(Year)

        # year_list.append(Year)
# for i in range(1, len(title_jump_list)):
#     print(title_jump_list[i])
#https://www.thepaper.cn/newsDetail_forward_15694196

print(year_list)
print(title_jump_list)
print(len(title_jump_list))
print(len(year_list))

Title_list=[]
Content_list=[]
ALL_list=[]

for i in title_jump_list:
    url="https://www.thepaper.cn/"+str(i)
    response=requests.get(url,headers=headers)
    data=response.text
    soup=BeautifulSoup(data,"html.parser")
    Each_Title=soup.select("body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > h1")
    if Each_Title:
        Each_Title=Each_Title[0]
        Each_Title=Each_Title.get_text()
        # print(Each_Title)
        Title_list.append(Each_Title)
    else:
        continue

    Each_Content=soup.select("body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > div.news_txt")
    if Each_Content:
        Each_Content=Each_Content[0]
        Each_Content=Each_Content.get_text().replace("(本文来自澎湃新闻，更多原创资讯请下载“澎湃新闻”APP)","").replace("\n","").replace(" ","").replace(u"\xa0","")
        # print(Each_Content)
        Content_list.append(Each_Content)
    else:
        continue

    ALL_list.append(
        {
            "事件标题":Each_Title,
            "事件内容":Each_Content
        }
    )

print(len(Title_list))
print(len(Content_list))
print(len(ALL_list))

for i in range(0,len(Title_list)):
    file_path= "C:/Users/OK/Desktop/知识图谱_任务/2网络攻击事件（2014-2017）/pachong/data/"+year_list[i]+"年网络攻击事件.csv"
    with open(file_path,"a",newline="",encoding="utf-8") as f:
        fieldnames=["事件标题","事件内容"]
        f_csv=csv.DictWriter(f,fieldnames=fieldnames)
        f_csv.writeheader()
        f_csv.writerow(
            {
                "事件标题":Title_list[i],
                "事件内容":Content_list[i]
            }
        )