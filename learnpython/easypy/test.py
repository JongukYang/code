from bs4 import BeautifulSoup
import urllib.request as req

url = "https://zum.com/"
# urlopen()으로 데이터 가져오기 
res = req.urlopen(url)
# BeautifulSoup으로 분석하기 
soup = BeautifulSoup(res, "html.parser")

# 원하는 데이터 추출하기 
results = soup.select('#app > div > main > div.issue-keyword > div.keyword-list > div.wrap-list > ol > li > a')


# list = soup.select("#app > div > main > div.issue-keyword > div.keyword-list > div > ol.list.left > li:nth-child(1)")

print(results)

#app > div > main > div.issue-keyword > div.keyword-list > div > ol.list.left > li:nth-child(1) > a