from django import forms
from payment.models import MpesaPayment
class paymentForm(forms.Form):
    class Meta:
        model = MpesaPayment
        fields = ('amount', 'phone_number',)