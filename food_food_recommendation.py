import requests as re
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.ptt.cc/bbs/Food/index.html")  # 開啟範例網址

titles = []
authors = []
dates = []
i = 0

while i <= 2:
    i += 1
    lp = driver.find_element(By.LINK_TEXT, "‹ 上頁")
    time.sleep(3)
    lp.click()

    res = re.get("https://www.ptt.cc/bbs/Food/index.html")
    soup = BeautifulSoup(res.text, features="html.parser")

    for item in soup.select(".r-ent"):
        title = item.select(".title")[0].text.strip()
        author = item.select(".author")[0].text.strip()
        date = item.select(".date")[0].text.strip()

        if title[0:4] == "[食記]":
            titles.append(title)
            authors.append(author)
            dates.append(date)

res_df = pd.DataFrame({"發文日期": dates, "標題": titles, "作者": authors})
print(res_df)

res_df.to_csv("./foodfood_list.csv", index=False, encoding="utf-8-sig")
