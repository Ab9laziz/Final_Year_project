from django.contrib import messages
from django.contrib.auth import get_user_model
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from portal.models import TrainingSession

from .index import DashboardView

User = get_user_model()


class TrainingSessionListView(DashboardView, ListView):
    model = TrainingSession
    template_name = 'player-dashboard/training-sessions/list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["playing_sessions"] = user.training_sessions_playing.all().order_by(
            "-pk")
        return context


class TrainingSessionDetailView(DashboardView, DetailView):
    model = TrainingSession
    context_object_name = 'fixture'
    template_name = 'player-dashboard/training-sessions/details.html'
