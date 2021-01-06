from django.urls import path

from ..views.payments import PaymentDetailView, PaymentListView

app_name = "payments"

urlpatterns = [
    path('all/', PaymentListView.as_view(), name='payments_list'),
    path('<int:pk>/details', PaymentDetailView.as_view(), name='payment_details'),
]
