import json
from django.db import models
from home.models import CommonInfo
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
User = get_user_model()
# Create your models here.
class FeeSetting(CommonInfo):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.amount


class PaymentManager(models.Manager):
    # saving the processed  payment to db
    def save_api_response(self, request, user=None):
        mpesa_body = request.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

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
        )
        if user:
            payment.user = request.user
            payment.save()
            payment.refresh_from_db()
        return payment

class MpesaPayment(CommonInfo):
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    payment_type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    organization_balance = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')

    objects = PaymentManager()

    def __str__(self):
        return f" {self.first_name} {self.amount}"

    def save(self, *args, **kwargs):

        try:
            qs = FeeSetting.objects.last()
        except:
            raise ObjectDoesNotExist("The query set does not exist")

        self.balance = qs.amount - self.amount
        super().save(*args, *kwargs)