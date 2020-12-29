from allauth.account.views import LoginView
from django.views.generic import TemplateView,UpdateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy


class UserAccountTemplateView(TemplateView):
    template_name = 'users/profile.html'


def logout_user(request):
    logout(request)
    return redirect('index')


def login_redirect(request):
    if request.user.role == 'player':
        return redirect('players:profile_update', pk=request.user.pk)
    elif request.user.role == 'admin':
        return redirect('dashboard:index:index')
    elif request.user.role == 'trainer':
        return redirect('trainer_dashboard:index:index')
    else:
        return redirect('index')



class LoginUserView(LoginView):
    def get_success_url(self):
        return reverse_lazy('login_redirect')


def register_redirect(request):
    if request.user.role == 'player':
        return redirect('players:profile_update', pk=request.user.pk)
    else:
        return redirect('index', pk=request.user.pk)

class RegisterUserView(UpdateView):
    def get_success_url(self):
        return reverse_lazy('register_redirect')