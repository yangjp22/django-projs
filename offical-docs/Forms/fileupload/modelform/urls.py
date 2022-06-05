from django.urls import path

from . import views


app_name = "modelform"
urlpatterns = [
    path('', views.index, name="index")
]