from django.urls  import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get-name/', views.get_name, name="get-name"),
    path('your-name/', views.get_name, name="your-name"),
    path('thanks/', views.thanks, name="thanks"),
    path('send-email/', views.send_email, name="send-email")
]