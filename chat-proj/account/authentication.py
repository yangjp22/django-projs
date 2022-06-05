from django.contrib.auth import views

class myLogin(views.LoginView):
    template_name = 'account/login.html'
    success_url = 'account/logout/'
    myNext = 'http://www.baidu.com'
    extra_context = {'myNext': myNext}

class myLogout(views.LogoutView):
    template_name = 'registration/logged_out.html'

    login_url = 'http://baidu.com'