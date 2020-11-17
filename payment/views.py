from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import paymentForm
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
import requests
from .stk import index


def lipa(request):
    if request.method == 'POST':
        form = paymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            phone_number = form.cleaned_data.get('phone_number')
            remit = index(phone_number, amount)
            # print (remit.response)
            print(phone_number, amount)
            return redirect('lipa')
    else:
        form = paymentForm(None)
        return render(request, 'payment/details_form.html', {'form':form})



