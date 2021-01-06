from django.contrib.auth import get_user_model
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from ..utils import send_welcome_email
from .index import DashboardView

User = get_user_model()


class TrainerCreateView(DashboardView, CreateView):
    model = User
    template_name = 'dashboard/users/trainers/add.html'
    fields = ('first_name', 'last_name', 'email',
              'phone_number', 'gender', 'group' ,'id_no', 'staff_id', )

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        random_password = get_random_string()
        user = form.save(commit=False)
        user.email = form.instance.email.lower()
        user.username = user.email
        user.set_password(random_password)
        user.role = 'trainer'
        user.save()

        send_welcome_email(user, random_password, self.request)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('dashboard:trainers:trainer_details', kwargs={'pk': self.object.pk})


class TrainerListView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'dashboard/users/trainers/list.html'
    queryset = User.objects.filter(role='trainer')


class TrainerDetailView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/trainers/details.html'


