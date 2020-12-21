from django.contrib import admin

from .models import ConsentForm, Fixture, TrainingSession

# Register your models here.
admin.site.register(ConsentForm)
admin.site.register(Fixture)
admin.site.register(TrainingSession)
