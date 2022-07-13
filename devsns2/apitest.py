# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request # 특정 url에 request를 날릴 수 있는 도구
from apiscret import secret_client_id, secret_client_secret

import json

# naver developer api 가져오는 부분
client_id = secret_client_id
client_secret = secret_client_secret

encText = urllib.parse.quote("한국")

# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)

rescode = response.getcode()
if(rescode==200): # 성공 코드: 200 번대 
    response_body = response.read()
    # json 파일 저장을 위해 아래 주석
    # print(response_body.decode('utf-8')) 
else:
    print("Error Code:" + rescode)


# json 파일 저장을 위해 아래 사용
resdata = response_body.decode('utf-8')
# with open('movie.json', 'w', encoding='UTF-8-sig') as file:
#     file.write(json.dumps(resdata, ensure_ascii=False)) # 

pythondata = json.loads(resdata)
data = pythondata['items']
print(data[0])
print(data[0]['title'])