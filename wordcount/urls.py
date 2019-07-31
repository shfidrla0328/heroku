from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('wordcount/', views.wordcount, name="wordcount"),
    path('result/', views.result, name="result"),
]