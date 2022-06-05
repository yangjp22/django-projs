from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cartDetail, name='cartDetail'),
    path('add/<int:productId>', views.cartAdd, name='cartAdd'),
    path('remove/<int:productId>', views.cartRemove, name='cartRemove'),

]