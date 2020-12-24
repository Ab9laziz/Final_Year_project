from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import TemplateView

User = get_user_model()


class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.role == 'trainer':
            return True
        return False


class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'trainer-dashboard/index.html'
