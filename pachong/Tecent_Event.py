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


for i in range(16,41):
    url="https://guanjia.qq.com/news/n0/list_0_"+str(i)+".html"
    response=requests.get(url,headers=headers)
    data=response.text
    soup=BeautifulSoup(data,"html.parser")
    for i in range(1,21):
        Title=soup.select("body > div.news_box > div.main > div.news_list > ul > li:nth-child("+str(i)+") > div.tabs_con > a")
        if Title:
            Title=Title[0]
            Title=Title["href"].replace("\n","").replace(" ","")
        else:
            continue

        #body > div.news_box > div.main > div.news_list > ul > li: nth - child(1) > div.tabs_con > span
        #body > div.news_box > div.main > div.news_list > ul > li:nth-child(20) > div.tabs_con > span
        Year=soup.select("body > div.news_box > div.main > div.news_list > ul > li:nth-child("+str(i)+") > div.tabs_con > span")
        if Year:
            Year=Year[0]
            Year=Year.get_text()
        else:
            continue



        title_jump_list.append(Title)
        year_list.append(Year)

        # year_list.append(Year)
# for i in range(1, len(title_jump_list)):
#     print(title_jump_list[i])
#https://www.thepaper.cn/newsDetail_forward_15694196

print(year_list)
print(title_jump_list)
print(len(title_jump_list))
print(len(year_list))



# Title_list=[]
# Content_list=[]
# ALL_list=[]
#
# for i in title_jump_list:
#     url="https://www.thepaper.cn/"+str(i)
#     response=requests.get(url,headers=headers)
#     data=response.text
#     soup=BeautifulSoup(data,"html.parser")
#     Each_Title=soup.select("body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > h1")
#     if Each_Title:
#         Each_Title=Each_Title[0]
#         Each_Title=Each_Title.get_text()
#         # print(Each_Title)
#         Title_list.append(Each_Title)
#     else:
#         continue
#
#     Each_Content=soup.select("body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > div.news_txt")
#     if Each_Content:
#         Each_Content=Each_Content[0]
#         Each_Content=Each_Content.get_text().replace("(????????????????????????????????????????????????????????????????????????APP)","").replace("\n","").replace(" ","").replace(u"\xa0","")
#         # print(Each_Content)
#         Content_list.append(Each_Content)
#     else:
#         continue
#
#     ALL_list.append(
#         {
#             "????????????":Each_Title,
#             "????????????":Each_Content
#         }
#     )
#
# print(len(Title_list))
# print(len(Content_list))
# print(len(ALL_list))
#
# for i in range(0,len(Title_list)):
#     file_path= "C:/Users/OK/Desktop/????????????_??????/2?????????????????????2014-2017???/pachong/data/"+year_list[i]+"?????????????????????.csv"
#     with open(file_path,"a",newline="",encoding="utf-8") as f:
#         fieldnames=["????????????","????????????"]
#         f_csv=csv.DictWriter(f,fieldnames=fieldnames)
#         f_csv.writeheader()
#         f_csv.writerow(
#             {
#                 "????????????":Title_list[i],
#                 "????????????":Content_list[i]
#             }
#         )