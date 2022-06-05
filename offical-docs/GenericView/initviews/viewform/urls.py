from django.urls import path

from . import views


app_name = 'viewform'
urlpatterns = [
    path('', views.index),
    path('form', views.MyFormView.as_view(), name="form"),
    path('publishers/', views.PublisherListView.as_view(), name="publishers")
]