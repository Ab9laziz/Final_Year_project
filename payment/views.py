from django.contrib import messages
from django.db.models import base
from payment.models import MpesaPayment, FeeSetting, User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PaymentForm
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
import requests
from .stk import make_payment
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

User = get_user_model()

def lipa(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            phone_number = form.cleaned_data.get('phone_number')
            formatted_number = phone_number
            if(phone_number[0] == '0'):
                new_character = '254'
                formatted_number = phone_number[:0] + new_character + phone_number[0+1:]
            elif(phone_number[0] == '7'):
                new_character = '2547'
                formatted_number = phone_number[:0] + new_character + phone_number[0+1:]
            elif(phone_number[0:4] == '254'):
                formatted_number = phone_number
            elif(phone_number[0:4] == '+254'):
                new_character = ''
                formatted_number = phone_number[:0] + new_character + phone_number[0+1:]
            user = request.user
            remit = make_payment(formatted_number, amount)
            balance = calculate_balance(request, amount)
            MpesaPayment.objects.create(amount=amount, phone_number=formatted_number, user=user, first_name=user.first_name, last_name=user.last_name, balance=balance)
            user = User.objects.filter(id=user.id).update(fee_balance=balance)

            messages.success(request, "Your fee payment has been saved.")
            return redirect('lipa')
        else:
            return render(request, 'payment/details_form.html', {'form':form})
    else:
        form = PaymentForm(None)
        return render(request, 'payment/details_form.html', {'form':form})


def calculate_balance(request, amount):
        user = request.user
        user = User.objects.get(id=user.id)
        balance = user.fee_balance - amount
        return balance

# def lipa(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             amount = form.cleaned_data.get('amount')
#             phone_number = form.cleaned_data.get('phone_number')
#             user = request.user
#             remit = make_payment(phone_number, amount)
#             MpesaPayment.objects.save_api_response(remit, user)
#             messages.success(request, "Your fee payment has been saved.")
#             return redirect('lipa')
#         else:
#             return render(request, 'payment/details_form.html', {'form':form})
#     else:
#         form = PaymentForm(None)
#         return render(request, 'payment/details_form.html', {'form':form})

class PaymentCreateView(CreateView):
    model = MpesaPayment
    form_class = PaymentForm
    template_name = 'payment/details_form.html'

    def form_valid(self, form):
        user = self.request.user
        payment = form.save(commit=False)
        payment.user = user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return render(self.request, 'payment/details_form.html')

