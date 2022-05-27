import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://m.zum.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

# results = soup.findAll('a','link_favorsch')
results = soup.select('#app > div > main > div.issue-keyword > div.keyword-list > div.wrap-list > ol > li > a')

# search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    # search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text())
    rank += 1

