from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('first-view', views.MyView.as_view(), name="first-view")
]