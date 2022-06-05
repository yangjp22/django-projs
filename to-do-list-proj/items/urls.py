from django.urls import re_path
from . import views

app_name='app_item'
urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^items/$', views.listItem, name='listItem'),
    re_path(r'^deletes/(?P<deleteId>\d+)/$', views.deleteItem, name='delete'),
]
