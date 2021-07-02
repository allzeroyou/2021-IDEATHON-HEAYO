"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from theapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.main, name="main"),
    path('cafe/',views.cafe, name="cafe"),
    path('food/',views.food, name="food"),
    path('movie/',views.movie, name="movie"),
    path('mypage/',views.mypage, name="mypage"),
    path('change/',views.change, name="change"),
    path('about/',views.about, name="about"),
    path('register/',views.register, name="register"),
    path('logged/',views.logged, name="logged"),
    path('kiosk_1/',views.kiosk_1, name="kiosk_1"),
    path('kiosk_2/',views.kiosk_2, name="kiosk_2"),
    path('kiosk_3/',views.kiosk_3, name="kiosk_3"),
    path('kiosk_4/',views.kiosk_4, name="kiosk_4"),
    path('kiosk_5/',views.kiosk_5, name="kiosk_5"),
    path('kiosk_6/',views.kiosk_6, name="kiosk_6"),
    path('kiosk_7/',views.kiosk_7, name="kiosk_7"),
    
]