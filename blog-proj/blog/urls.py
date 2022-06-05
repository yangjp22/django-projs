from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.postList, name='list'),
    path('tag/<slug:tagSlug>/', views.postList, name='listByTag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.postDetail, name='detail'),
    path('share/<int:postId>/', views.postShare, name='share'),
]
