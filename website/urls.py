
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home_page,name='home'),
    path('news', views.news,name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('projects', views.projects, name='projects'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('contact/', views.contact_form, name='contact_form'),
    path('category/<int:category_id>/', views.news_by_category, name='news_by_category'),
    # path('services/', views.services, name='services'),
  
]
