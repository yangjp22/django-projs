from django.urls import path
from . import views


app_name ='shop'
urlpatterns = [
    path('', views.productList, name='productList'),
    path('<slug:categorySlug>/', views.productList, name='productListByCategory'),
    path('<int:id>/<slug:slug>/', views.productDetail, name='productDetail'),
]
