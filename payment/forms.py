from django import forms
from payment.models import MpesaPayment
class PaymentForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    phone_number = forms.CharField(max_length=15)