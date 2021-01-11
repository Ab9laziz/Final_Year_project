from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from portal.models import Fixture
from portal.forms import FixtureForm
from .index import DashboardView
from django.contrib.auth import get_user_model

User = get_user_model()



class FixtureCreateView(DashboardView, CreateView):
    model = Fixture
    form_class = FixtureForm
    template_name = 'dashboard/fixtures/add.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = self.request.user
        fixture = form.save(commit=False)
        fixture.added_by = user
        fixture.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, "Fixture Added Successfully")
        return reverse_lazy("trainer_dashboard:fixtures:fixture_add_players", kwargs={'pk': self.object.pk})


class FixtureAddPlayersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'trainer-dashboard/fixtures/select-players.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = Fixture.objects.get(
            id=self.kwargs['pk'])
        fixture_users = context['fixture'].starting_players.all() | context['fixture'].subtitutes.all()
        context['users'] = User.objects.exclude(id__in=fixture_users).filter(role="player", is_active=True)
        return context

# add players to an existing fixture


class FixtureEditPlayersView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'trainer-dashboard/fixtures/add-players.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = Fixture.objects.get(
            id=self.kwargs['pk'])
        fixture_users = context['fixture'].starting_players.all() | context['fixture'].subtitutes.all()
        context['users'] = User.objects.exclude(id__in=fixture_users).filter(role="player", is_active=True)
        return context


class FixtureAddSubtitutesView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'trainer-dashboard/fixtures/select-subtitutes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = Fixture.objects.get(
            id=self.kwargs['pk'])
        fixture_users = context['fixture'].starting_players.all() | context['fixture'].subtitutes.all()
        context['users'] = User.objects.exclude(id__in=fixture_users).filter(role="player", is_active=True)
        return context

# add subtitutes to an existing fixture


class FixtureEditSubtitutesView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'trainer-dashboard/fixtures/add-subtitutes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixture"] = Fixture.objects.get(
            id=self.kwargs['pk'])
        fixture_users = context['fixture'].starting_players.all() | context['fixture'].subtitutes.all()
        context['users'] = User.objects.exclude(id__in=fixture_users).filter(role="player", is_active=True)
        return context


class FixtureUpdateView(DashboardView, UpdateView):
    model = Fixture
    fields = ('name', 'description', 'date', 'picture')
    template_name = 'dashboard/fixtures/edit.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = self.request.user
        fixture = form.save(commit=False)
        fixture.updated = user
        fixture.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, "Fixture updated")
        return reverse_lazy("trainer_dashboard:fixtures:fixture_details", kwargs={'pk': self.object.pk})

class FixtureListView(DashboardView, ListView):
    model = Fixture
    context_object_name = 'fixtures'
    template_name = 'trainer-dashboard/fixtures/list.html'


class FixtureDetailView(DashboardView, DetailView):
    model = Fixture
    context_object_name = 'fixture'
    template_name = 'trainer-dashboard/fixtures/details.html'
