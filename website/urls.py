
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home_page,name='home'),
    path('news', views.news,name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
  
]
