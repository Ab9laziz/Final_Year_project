from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from django.forms import widgets

from .models import Fixture, TrainingSession


class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = ('name', 'description', 'date', 'picture')
        widgets = {
            'date': DateTimePickerInput()
        }


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ('name', 'description', 'date', 'picture')
        widgets = {
            'date': DateTimePickerInput()
        }
