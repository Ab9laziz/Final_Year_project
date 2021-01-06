from django.urls import reverse_lazy

from .index import DashboardView
from django.contrib import messages
from django.views.generic import DetailView, ListView
from payment.models import FeeSetting, MpesaPayment





class PaymentListView(DashboardView, ListView):
    model = MpesaPayment
    context_object_name = 'payments'
    template_name = 'player-dashboard/payments/list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["fee_setting"] = FeeSetting.objects.last()
        context["payments"] = MpesaPayment.objects.all().filter(user=user).order_by('-pk')
        return context


class PaymentDetailView(DashboardView, DetailView):
    model = MpesaPayment
    context_object_name = 'payment'
    template_name = 'player-dashboard/payments/details.html'
