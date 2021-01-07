from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group

from django.views.generic import TemplateView
from portal.models import TrainingSession, Fixture

User = get_user_model()


class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.role == 'trainer':
            return True
        return False


class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'trainer-dashboard/index.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["assigned_sessions"] = user.training_sessions_assigned.all().order_by("-pk")[:10]
        context["added_sessions"] = user.training_sessions_created.all().order_by("-pk")[:10]
        context["fixtures"] = Fixture.objects.all().order_by("-pk")[:10]
        context["recent_players"] = User.objects.filter(group=user.group)[:5]
        return context
