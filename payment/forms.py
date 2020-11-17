from django import forms

class paymentForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    phone_number = forms.CharField(min_length=12,max_length=12)

    class Meta:
        fields ='__all__'