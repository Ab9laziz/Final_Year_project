from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView
from users.models import ConsentForm, PlayerMedicalRecord, PlayerProfile

from .index import DashboardView

User = get_user_model()


class PlayerListView(DashboardView, ListView):
    model = User
    context_object_name = 'users'
    queryset = User.objects.filter(role='player')
    template_name = 'dashboard/users/players/list.html'


class PlayerDetailView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/players/details.html'

    def get_context_data(self, **kwargs):
        user_id = self.object.id
        context = super().get_context_data(**kwargs)
        context["profile"] = PlayerProfile.objects.get(user=user_id)
        context["medical_records"] = PlayerMedicalRecord.objects.filter(
            user=user_id)
        context["consent_form"] = ConsentForm.objects.get(user=user_id)
        return context


class PlayerSuspendView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'
