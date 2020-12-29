from django.views.generic import DetailView, ListView
from portal.models import Fixture

from .index import DashboardView


class FixtureListView(DashboardView, ListView):
    model = Fixture
    context_object_name = 'fixtures'
    template_name = 'player-dashboard/fixtures/list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["fixtures_playing"] = user.fixtures_playing.all()
        context["fixtures_subtituting"] = user.fixtures_subtituting.all()
        return context

class FixtureDetailView(DashboardView, DetailView):
    model = Fixture
    context_object_name = 'fixture'
    template_name = 'player-dashboard/fixtures/details.html'
