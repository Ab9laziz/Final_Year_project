from django.contrib import admin

from .models import FeeSetting, MpesaPayment

# Register your models here.
admin.site.register(FeeSetting)
admin.site.register(MpesaPayment)
