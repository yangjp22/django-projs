from django.urls import path
from . import views

app_name = 'image'
urlpatterns = [
    path('create/', views.imageCreate, name='create'),
    path('detail/<id>/<slug>/', views.imageDetail, name='detail'),
    path('like/', views.imageLike, name='like'),
    path('', views.imageList, name='list'),
]
