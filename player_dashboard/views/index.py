from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import TemplateView

User = get_user_model()


class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.role == 'player':
            return True
        return False


class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'player-dashboard/index.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["sessions"] = user.training_sessions_playing.all().order_by(
            "-pk")[:10]
        context["fixtures_playing"] = user.fixtures_playing.all().order_by("-pk")[:10]
        context["fixtures_subtituting"] = user.fixtures_subtituting.all().order_by("-pk")[:10]
        return context
