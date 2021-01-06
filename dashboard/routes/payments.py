from django.urls import path

from ..views.payments import (FeeSettingCreateView, FeeSettingListView,
                              FeeSettingUpdateView, PaymentDetailView,
                              PaymentListView)

app_name = "payments"

urlpatterns = [
    path('all/', PaymentListView.as_view(), name='payments_list'),
    path('<int:pk>/details', PaymentDetailView.as_view(), name='payment_details'),
    path('fee-settings/add/', FeeSettingCreateView.as_view(), name='fee_setting_add'),
    path('fee-settings/list/', FeeSettingListView.as_view(), name='fee_settings_list'),
    path('fee-settings/<int:pk>/edit/', FeeSettingUpdateView.as_view(), name='fee_setting_edit'),
]
