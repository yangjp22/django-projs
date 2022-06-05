from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('search/home/', views.searchHome, name='searchHome'),
    path('search/craigslist/', views.craigslist, name='craigslist'),
]
