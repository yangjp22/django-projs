from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contract
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required


def userLogin(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            cd = loginForm.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully.')
                else:
                    return HttpResponse('Disabled account.')
            else:
                return HttpResponse('Username or password error.')
    else:
        loginForm = LoginForm()
    return render(request, 'account/login.html', {'form': loginForm})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})

def register(request):
    if request.method == 'POST':
        userForm = UserRegistrationForm(request.POST)
        if userForm.is_valid():
            newUser = userForm.save(commit=False)
            newUser.set_password(userForm.cleaned_data['password'])
            newUser.save()
            Profile.objects.create(user=newUser)
            return render(request, 'account/registerDone.html', {'newUser':newUser})
    else:
        userForm = UserRegistrationForm()
    return render(request, 'account/register.html', {'userForm': userForm})

@login_required
def edit(request):
    if request.method == "POST":
        userForm = UserEditForm(instance=request.user, data=request.POST)
        profileForm = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Error updating your profile')
    else:
        userForm = UserEditForm(instance=request.user)
        profileForm = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'userForm': userForm, 'profileForm':profileForm})

@login_required
def userList(request):
    users = User.objects.filter(is_active=True).order_by('username')
    return render(request, 'account/user/list.html', {'section': 'people', 'users':users})

@login_required
def userDetail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user':user})


@ajax_required
@login_required
@require_POST
def userFollow(request):
    userId = request.POST.get('id')
    action = request.POST.get('action')
    if userId and action:
        try:
            user = User.objects.get(id=userId)
            if action == 'follow':
                Contract.objects.get_or_create(userFrom=request.user, userTo=user)
            else:
                Contract.objects.filter(userFrom=request.user, userTo=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'ko'})
        except:
            pass
    return JsonResponse({'status': 'ko'})








