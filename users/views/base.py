from allauth.account.views import LoginView
from django.views.generic import TemplateView,UpdateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth, messages


User = auth.get_user_model()

class UserAccountTemplateView(TemplateView):
    template_name = 'users/profile.html'


def logout_user(request):
    logout(request)
    return redirect('index')


def login_redirect(request):
    if request.user.role == 'player':
        return redirect('player_dashboard:index:index')
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

class UserDetailView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/profile/details.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["user"] = User.objects.get(id=user.id)
        return context

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('first_name','last_name','email','phone_number','gender','photo')
    template_name = 'users/profile/edit.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.email.lower()
        user.save()

        return super(UserProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Your Details have been successfully updated.")
        return reverse_lazy("users:user_profile")