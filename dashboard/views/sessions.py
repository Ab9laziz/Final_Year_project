from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from portal.models import TrainingSession

from .index import DashboardView
from django.contrib.auth import get_user_model

User = get_user_model()


class TrainingSessionCreateView(DashboardView, CreateView):
    model = TrainingSession
    fields = ('name', 'description', 'date', 'picture')
    template_name = 'dashboard/training-sessions/add.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = self.request.user
        TrainingSession = form.save(commit=False)
        TrainingSession.added_by = user
        TrainingSession.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, "Training Session Added Successfully")
        return reverse_lazy("dashboard:sessions:session_add_players", kwargs={'pk': self.object.pk})


class TrainingSessionAddPlayersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'dashboard/training-sessions/select-players.html'

    def get_queryset(self):
        return User.objects.exclude(training_sessions_playing=self.kwargs['pk']).filter(role="player")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = TrainingSession.objects.get(
            id=self.kwargs['pk'])
        return context

# add players to an existing TrainingSession


class TrainingSessionEditPlayersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'dashboard/training-sessions/add-players.html'

    def get_queryset(self):
        return User.objects.exclude(training_sessions_playing=self.kwargs['pk']).filter(role="player")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = TrainingSession.objects.get(
            id=self.kwargs['pk'])
        return context


class TrainingSessionAddTrainersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'dashboard/training-sessions/select-trainers.html'

    def get_queryset(self):
        return User.objects.exclude(training_sesssions_assigned=self.kwargs['pk']).filter(role="trainer")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = TrainingSession.objects.get(
            id=self.kwargs['pk'])
        return context

# add Trainers to an existing TrainingSession


class TrainingSessionEditTrainersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'dashboard/training-sessions/add-trainers.html'

    def get_queryset(self):
        return User.objects.exclude(training_sesssions_assigned=self.kwargs['pk']).filter(role="trainer")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = TrainingSession.objects.get(
            id=self.kwargs['pk'])
        return context


class TrainingSessionUpdateView(DashboardView, UpdateView):
    model = TrainingSession
    fields = ('name', 'description', 'date', 'picture')
    template_name = 'dashboard/training-sessions/edit.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = self.request.user
        TrainingSession = form.save(commit=False)
        TrainingSession.updated = user
        TrainingSession.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, "Training Session updated")
        return reverse_lazy("dashboard:sessions:session_details", kwargs={'pk': self.object.pk})


class TrainingSessionListView(DashboardView, ListView):
    model = TrainingSession
    context_object_name = 'fixtures'
    template_name = 'dashboard/training-sessions/list.html'


class TrainingSessionDetailView(DashboardView, DetailView):
    model = TrainingSession
    context_object_name = 'fixture'
    template_name = 'dashboard/training-sessions/details.html'
