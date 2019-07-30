from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('blogapp/create', views.create, name="create"),
    path('write/', views.write, name="write"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/delete/', views.update, name="update"),
]