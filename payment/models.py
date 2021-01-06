import json
from django.db import models
from home.models import CommonInfo
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
User = get_user_model()
# Create your models here.
class FeeSetting(CommonInfo):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.amount


class PaymentManager(models.Manager):
    # saving the processed  payment to db
    def save_api_response(self, response, user):
        mpesa_body = response.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)
        # mpesa_payment = response.json()
        print(f"mpesa payment {mpesa_payment}")

        payment = self.create(
            first_name = mpesa_payment['FirstName'],
            last_name=mpesa_payment['LastName'],
            middle_name=mpesa_payment['MiddleName'],
            description=mpesa_payment['TransID'],
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            organization_balance=mpesa_payment['OrgAccountBalance'],
            transaction_type=mpesa_payment['TransactionType'],
            user = user
        )
        payment.save()
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))

class MpesaPayment(CommonInfo):
    amount = models.PositiveIntegerField()
    description = models.TextField(null=True)
    payment_type = models.TextField(null=True)
    reference = models.TextField(null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    organization_balance = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')

    # objects = PaymentManager()

    def __str__(self):
        return f" {self.first_name} {self.amount}"
