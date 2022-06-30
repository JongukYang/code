from django.shortcuts import redirect, render
# 로그인 로그아웃 할 때 꼭 필요한거
from django.contrib import auth

# Create your views here.
def login(request):
    # request == POST : 로그인
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # authenticate 메소드는 username,password가 일치하는 객체를 반환함(만약 없으면 NONE반환)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    # request == GET : 로그아웃
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
    
