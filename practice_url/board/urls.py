from django.urls import path
from board import views

urlpatterns = [
    path('', views.board), # boards/ 뒤에 아무것도 안 썼다고 가정했을 때 실행되는 처음 화면
    path('first/', views.boardfirst), # http://127.0.0.1:8000/boards/first url을 실행한다는 뜻
]

