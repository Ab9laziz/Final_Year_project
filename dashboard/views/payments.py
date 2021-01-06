from django.urls import reverse_lazy

from .index import DashboardView
from django.contrib import messages
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from payment.models import FeeSetting, MpesaPayment


class FeeSettingCreateView(DashboardView, CreateView):
    model = FeeSetting
    fields = ('amount',)
    template_name = 'dashboard/payments/settings/add.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Fee Setting Added Successfully")
        return reverse_lazy('dashboard:payments:fee_settings_list')


class FeeSettingUpdateView(DashboardView, UpdateView):
    model = FeeSetting
    fields = ('amount',)
    template_name = 'dashboard/payments/settings/add.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Fee Setting Added Successfully")
        return reverse_lazy('dashboard:payments:fee_settings_list')


class FeeSettingListView(DashboardView, ListView):
    model = FeeSetting
    template_name = 'dashboard/payments/settings/list.html'
    context_object_name = 'settings'


class PaymentListView(DashboardView, ListView):
    model = MpesaPayment
    context_object_name = 'payments'
    template_name = 'dashboard/payments/list.html'


class PaymentDetailView(DashboardView, DetailView):
    model = MpesaPayment
    context_object_name = 'payment'
    template_name = 'dashboard/payments/details.html'
