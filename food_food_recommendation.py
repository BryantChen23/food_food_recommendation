import requests as re
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import progressbar


titles = []
authors = []
dates = []

with progressbar.ProgressBar(max_value=7002) as bar:
    for i in range(7002, 5000, -1):
        # 抓取每頁 標題、日期、作者
        res = re.get("https://www.ptt.cc/bbs/Food/index%d.html" % i)
        soup = BeautifulSoup(res.text, features="html.parser")
        for item in soup.select(".r-ent"):
            title = item.select(".title")[0].text.strip()
            author = item.select(".author")[0].text.strip()
            date = item.select(".date")[0].text.strip()

            if title[0:4] == "[食記]":
                titles.append(title)
                authors.append(author)
                dates.append(date)
        time.sleep(0.1)
        bar.update(i)

res_df = pd.DataFrame({"發文日期": dates, "標題": titles, "作者": authors})
print(len(res_df))
res_df.to_csv("./foodfood_list.csv", index=False, encoding="utf-8-sig")
