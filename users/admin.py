from django.contrib import admin

from .models import (ConsentForm, PlayerMedicalRecord, PlayerProfile,
                     UserAccount)

# Register your models here.

admin.site.register(ConsentForm)
admin.site.register(PlayerMedicalRecord)
admin.site.register(PlayerProfile)
admin.site.register(UserAccount)
