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
            user = request.user
            remit = make_payment(phone_number, amount) 
            balance = calculate_balance(amount)
            MpesaPayment.objects.create(amount=amount, phone_number=phone_number, user=user, first_name=user.first_name, last_name=user.last_name)
            # user = User.objects.get(id=user.id)
            # user.update()

            messages.success(request, "Your fee payment has been saved.")
            return redirect('lipa')
        else:
            return render(request, 'payment/details_form.html', {'form':form})
    else:
        form = PaymentForm(None)
        return render(request, 'payment/details_form.html', {'form':form})


def calculate_balance(amount):
        try:
            qs = FeeSetting.objects.last()
        except:
            raise ObjectDoesNotExist("The query set does not exist")

        balance = qs.amount - amount
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

