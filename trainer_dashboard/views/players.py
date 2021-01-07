from django.views.generic import ListView
from .index import DashboardView
from django.contrib.auth import get_user_model

User = get_user_model()


class PlayerListView(DashboardView, ListView):
    model = User
    template_name = 'trainer-dashboard/players/list.html'


    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(group=user.group).order_by("-id")
        return context
