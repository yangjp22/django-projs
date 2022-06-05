from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy

urlpatterns = [
    # path('login/', views.userLogin, name='login')
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('passwordChange/', auth_view.PasswordChangeView.as_view(success_url='done/'), name='passwordChange'),
    path('passwordChange/done/', auth_view.PasswordChangeDoneView.as_view(), name='passwordChangeDone'),
    path('passwordReset/', auth_view.PasswordResetView.as_view(success_url='done/'), name='passwordReset'),
    path('passwordReset/done/', auth_view.PasswordResetDoneView.as_view(), name='passwordResetDone'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(success_url=reverse_lazy('passwordResetComplete')), name='passwordResetConfirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(), name='passwordResetComplete'),
    path('register/', views.register,  name='register'),
    path('edit/', views.edit, name='edit'),
    path('users/', views.userList, name='userList'),
    path('users/<username>/', views.userDetail, name='userDetail'),
    path('follow/', views.userFollow, name='Follow'),
]