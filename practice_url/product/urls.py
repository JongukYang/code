from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist), # products/ 뒤에 아무것도 안 썼다고 가정했을 때 실행되는 처음 화면
    path('first/', views.productfirst),
]

