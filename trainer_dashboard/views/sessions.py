from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from portal.models import TrainingSession
from portal.forms import TrainingSessionForm
from .index import DashboardView
from django.contrib.auth import get_user_model

User = get_user_model()


class TrainingSessionCreateView(DashboardView, CreateView):
    model = TrainingSession
    form_class = TrainingSessionForm
    template_name = 'dashboard/training-sessions/add.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = self.request.user
        TrainingSession = form.save(commit=False)
        TrainingSession.added_by = user
        TrainingSession.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, "Training Session Added Successfully")
        return reverse_lazy("trainer_dashboard:sessions:session_add_players", kwargs={'pk': self.object.pk})


class TrainingSessionAddPlayersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'trainer-dashboard/training-sessions/select-players.html'

    def get_queryset(self):
        user = self.request.user
        return User.objects.exclude(training_sessions_playing=self.kwargs['pk'], is_active=False).filter(role="player", group=user.group)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = TrainingSession.objects.get(
            id=self.kwargs['pk'])
        return context

# add players to an existing TrainingSession


class TrainingSessionEditPlayersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'trainer-dashboard/training-sessions/add-players.html'

    def get_queryset(self):
        user = self.request.user
        return User.objects.exclude(training_sessions_playing=self.kwargs['pk']).filter(role="player", is_active=True, group=user.group)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = TrainingSession.objects.get(
            id=self.kwargs['pk'])
        return context


class TrainingSessionAddTrainersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'trainer-dashboard/training-sessions/select-trainers.html'

    def get_queryset(self):
        user = self.request.user
        return User.objects.exclude(training_sessions_assigned=self.kwargs['pk']).filter(role="trainer", is_active=True, group=user.group)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = TrainingSession.objects.get(
            id=self.kwargs['pk'])
        return context

# add Trainers to an existing TrainingSession


class TrainingSessionEditTrainersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'trainer-dashboard/training-sessions/add-trainers.html'

    def get_queryset(self):
        user = self.request.user
        return User.objects.exclude(training_sessions_assigned=self.kwargs['pk']).filter(role="trainer", is_active=True, group=user.group)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = TrainingSession.objects.get(
            id=self.kwargs['pk'])
        return context


class TrainingSessionUpdateView(DashboardView, UpdateView):
    model = TrainingSession
    form_class = TrainingSessionForm
    template_name = 'dashboard/training-sessions/edit.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = self.request.user
        TrainingSession = form.save(commit=False)
        TrainingSession.updated = user
        TrainingSession.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, "Training Session updated")
        return reverse_lazy("trainer_dashboard:sessions:session_details", kwargs={'pk': self.object.pk})


class TrainingSessionListView(DashboardView, ListView):
    model = TrainingSession
    template_name = 'trainer-dashboard/training-sessions/list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["assigned_sessions"] = user.training_sessions_assigned.all().order_by(
            "-pk")
        context["added_sessions"] = user.training_sessions_created.all().order_by(
            "-pk")
        return context


class TrainingSessionDetailView(DashboardView, DetailView):
    model = TrainingSession
    context_object_name = 'fixture'
    template_name = 'trainer-dashboard/training-sessions/details.html'
