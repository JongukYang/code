"""blogproject URL Configuration

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
import django
from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form을 이용한 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    # django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # detail 페이지, 내가 가고 싶은 블로그 글 찾아 들어가기
    # 추가적인 정보가 필요함 <> 안에 입력하게 됨
    # blog_id 는 int형 변수로써 detail 함수에 넘길 값임 (ex) 1, 2, 3 이런식으로 들어가는 값이 전달됨
    path('detail/<int:blog_id>', views.detail, name='detail'),
    
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),

    # media 파일에 접근할 수 있는 url로 추가해주어야함
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 위와 아래는 같음
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)