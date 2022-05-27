# 파이썬의 f string 을 사용하기 위해선 문자열 앞에 f를 붙인다
# json = Javascript Object Notation

import requests
import json

city = "Seoul"
apikey = "ab43866d2f081a2a19c95953f71bb141"
temp = "metric"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang=kr&units={temp}"

# http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=ab43866d2f081a2a19c95953f71bb141

result = requests.get(api)
print(result.text)
data = json.loads(result.text) 

# print(type(result.text))
print(type(data))

print(data["name"],"의 날씨입니다.")
print("날씨는 ",data["weather"][0]["description"],"입니다.")
print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
# 습도 : main - humidity
print("습도는 ",data["main"]["humidity"],"입니다.")
# 기압 : main - pressure
print("기압은 ",data["main"]["pressure"],"입니다.")
# 풍향 : wind - deg
print("풍향은 ",data["wind"]["deg"],"입니다.")
# 풍속 : wind - speed
print("풍속은 ",data["wind"]["speed"],"입니다.")