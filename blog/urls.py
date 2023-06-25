from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('faq/', views.faq, name='faq' ),
    path('post/new/',views.new_post, name='new_post'),
    path('post/<pk>/',views.post_details, name='post_details'),   
]