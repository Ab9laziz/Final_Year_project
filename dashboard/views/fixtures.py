from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from portal.models import Fixture

from .index import DashboardView
from django.contrib.auth import get_user_model

User = get_user_model()


class FixtureCreateView(DashboardView, CreateView):
    model = Fixture
    fields = ('name', 'description', 'date', 'picture')
    template_name = 'dashboard/fixtures/add.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = self.request.user
        fixture = form.save(commit=False)
        fixture.added_by = user
        fixture.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, "Fixtured Added Successfully")
        return reverse_lazy("dashboard:fixtures:fixture_details", kwargs={'pk': self.object.pk})


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
        return reverse_lazy("dashboard:fixtures:fixture_details", kwargs={'pk': self.object.pk})


class FixtureListView(DashboardView, ListView):
    model = Fixture
    context_object_name = 'fixtures'
    template_name = 'dashboard/fixtures/list.html'


class FixtureDetailView(DashboardView, DetailView):
    model = Fixture
    context_object_name = 'fixture'
    template_name = 'dashboard/fixtures/details.html'
