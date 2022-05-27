"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views # myapp.views 의 내용을 가져와 사용하기 위해

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', myapp.views.home),
    path('', myapp.views.home, name='hello world'),
    path('test/', myapp.views.test, name='test'),
]

# 현재 우리 프로젝트의 url = http://127.0.0.1:8000/
# http://127.0.0.1:8000/home 
# '' 안에 아무 주소도 주지 않는다면 그냥 http://127.0.0.1:8000/ 주소로
# 들어갔을 때 바로 myapp의 views 안에 home라는 함수를 실행한다는 뜻
# name = 'abc' -> 그냥 url의 이름, 써도 그만 안써도 그만

# 순서 : 
# 1. 우리가 get 요청을 함 
# 2. urls.py 에서 url요청을 받고 myapp.views.test함수를 실행하게 됨
# 3. myapp.views에서 그것이 무슨 함수인지 체크 후
# 4. test.html파일을 연다
