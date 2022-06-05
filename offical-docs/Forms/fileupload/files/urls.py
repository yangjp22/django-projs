from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.uploadFile, name='upload'),
    path('upload/success/', views.success, name='success')
]