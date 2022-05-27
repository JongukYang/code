from django.shortcuts import redirect, render
# 이미 저장된 회원인지 아닌지를 판별하기 위해 auth 사용, 데베에서 판단 및 로그인/로그아웃 
# 기능 실행 가능, 장고에서 지원해줌
from django.contrib import auth
# 우리가 전에 만들었던 슈퍼유저의 계정은 장고의 User에 저장되어 있음
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    # 로그인 함수는 POST 요청이 들어오면 로그인 처리 해줌
    if request.method == 'POST':
        # 먼저 POST로 넘겨온 것들을 저장
        userid = request.POST['username']
        pwd = request.POST['password']
        # 사용자가 데이터베이스에서 이미 저장되어있는지 판별하기 위해 사용
        user = auth.authenticate(request, username=userid, password=pwd)
        # authenticate 함수는 이미 저장되어 있는 user 객체를 반환하거나 none 을 반환
        #만약 user 가 이미 저장되어 있다면
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        # 만약 없다면?
        else:
            return render(request, 'login.html')

    # GET 요청이 들어오면 login form 을 담고 있는 login.html을 띄워주는 역할
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')