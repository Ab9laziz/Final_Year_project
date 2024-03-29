from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.base import Model
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
from portal.models import ConsentForm, TrainingSession, Fixture

User = get_user_model()


class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == 'admin':
            return True
        return False


class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_sessions"] = TrainingSession.objects.all().order_by('-created_on')[:5]
        context["recent_fixtures"] = Fixture.objects.all().order_by('-created_on')[:5]
        context["recent_players"] = User.objects.filter(role='player').order_by('-date_joined')[:5]
        context["recent_trainers"] = User.objects.filter(role='trainer').order_by('-date_joined')[:5]
        return context
    


class UserConfirmSuspendView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'


class ConsentFormCreateView(DashboardView, CreateView):
    model = ConsentForm
    fields = ('document',)
    template_name = 'dashboard/consent-forms/add.html'

    def get_success_url(self) -> str:
        return reverse_lazy('dashboard:index:consent_form_details', kwargs={'pk': self.object.pk})


class ConsentFormListView(DashboardView, ListView):
    model = ConsentForm
    context_object_name = 'forms'
    template_name = 'dashboard/consent-forms/list.html'


class ConsentFormDetailView(DashboardView, DetailView):
    model = ConsentForm
    context_object_name = 'form'
    template_name = 'dashboard/consent-forms/details.html'


class ConsentFormUpdateView(DashboardView, UpdateView):
    model = ConsentForm
    fields = ('document',)
    template_name = 'dashboard/consent-forms/edit.html'

    def get_success_url(self) -> str:
        return reverse_lazy('dashboard:index:consent_form_details', kwargs={'pk': self.object.pk})
