from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.forms import BaseModelForm
from django.forms.forms import Form
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView
from payment.models import FeeSetting
from users.forms import PlayerSignUpForm
from users.models import ConsentForm, PlayerMedicalRecord, PlayerProfile
from users.views.base import register_redirect

User = get_user_model()


class SignUpView(FormView):
    template_name = 'users/players/signup.html'
    form_class = PlayerSignUpForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['email'].lower()
        raw_password = data['password1']

        user = User.objects.create_user(
            username=username,
            email=data['email'],
            password=raw_password
        )
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.gender = data['gender']
        user.role = 'player'
        user.date_of_birth = data['date_of_birth']
        # get the current fees and create the player's profile with current balance as the fee setting
        try:
            qs = FeeSetting.objects.last()
        except FeeSetting.DoesNotExist:
            return "There's no fee amount to pay set."
        user.fee_balance = qs.amount
        user.save()

        # create a profile instance once registered
        player_profile, created = PlayerProfile.objects.get_or_create(user=user)
        player_profile.save()

        # create a consent form instance once registered
        consent_form, created = ConsentForm.objects.get_or_create(user=user)
        consent_form.save()

        auth_user = authenticate(username=username, password=raw_password)
        login(self.request, auth_user)

        return super(SignUpView, self).form_valid(form)

    def get_success_url(self):
        user = self.request.user
        if user.role == 'player':
            return reverse_lazy('players:profile_update', kwargs={'pk': user.pk})


class ProfileUpdateView(UpdateView):
    template_name = 'users/players/profile/update.html'
    model = PlayerProfile
    context_object_name = 'player'
    fields = ('estate', 'guardian_name',
              'guardian_email', 'guardian_phone_number')

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk']).player_profile

    def get_success_url(self) -> str:
        return reverse_lazy('players:medical_record_add')


class MedicalRecordCreateView(CreateView):
    template_name = 'users/players/medical-records/add.html'
    model = PlayerMedicalRecord
    context_object_name = 'player'
    fields = ('description', 'special_instruction', 'doctor_name',
              'doctor_phone_number', 'doctor_phone_number')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        medical_record = form.save(commit=False)
        medical_record.user = self.request.user
        medical_record.save()

        return super(MedicalRecordCreateView, self).form_valid(form)


    def get_success_url(self) -> str:
        user = self.request.user
        messages.success(self.request, "Medical Record Successfully added")
        return reverse_lazy('players:consent_form_upload', kwargs={'pk': user.pk})


class MedicalRecordUpdateView(UpdateView):
    template_name = 'users/players/medical-records/edit.html'
    model = PlayerMedicalRecord
    context_object_name = 'player'
    fields = ('description', 'special_instruction', 'doctor_name',
              'doctor_phone_number', 'doctor_phone_number')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        medical_record = form.save(commit=False)
        medical_record.user = self.request.user
        medical_record.save()

        return super(MedicalRecordUpdateView, self).form_valid(form)

    def get_success_url(self) -> str:
        user = self.request.user
        messages.success(self.request, "Medical Record Successfully updated")
        return reverse_lazy('players:medical_record_details', kwargs={'pk': user.pk})


class ConsentFormUploadView(UpdateView):
    template_name = 'users/players/consent-forms/add.html'
    model = ConsentForm
    context_object_name = 'player'
    fields = ('scanned_consent_form',)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        consent_form = form.save(commit=False)

        consent_form.user.is_active = False
        print(consent_form.user.is_active)
        consent_form.user.save()
        consent_form.save()

        return super(ConsentFormUploadView, self).form_valid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk']).consent_form

    def get_success_url(self) -> str:
        messages.success(
            self.request, "Successfully registered, an activation email will be sent to your inbox once your details have been approved.")
        return reverse_lazy("home:index")
