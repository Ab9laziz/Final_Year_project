from django.views.generic import DetailView, ListView
from portal.models import Fixture

from .index import DashboardView


class FixtureListView(DashboardView, ListView):
    model = Fixture
    context_object_name = 'fixtures'
    template_name = 'trainer-dashboard/fixtures/list.html'


class FixtureDetailView(DashboardView, DetailView):
    model = Fixture
    context_object_name = 'fixture'
    template_name = 'trainer-dashboard/fixtures/details.html'
