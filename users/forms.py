from django.forms import ValidationError, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from bootstrap_datepicker_plus import  DatePickerInput
User = get_user_model()


class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'photo', 'phone_number', 'email',)


class PlayerSignUpForm(UserCreationForm):
    # gender = forms.CharField(widget=forms.CharField(attrs={'placeholder':'Enter Your Gender'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'email', 'phone_number', 'date_of_birth', 'group', )

        widgets = {
            'date_of_birth': DatePickerInput()
        }

    def clean(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError('A user with this email already exists.')
        return self.cleaned_data
