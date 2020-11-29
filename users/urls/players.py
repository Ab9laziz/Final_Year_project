from django.urls import path

from ..views.players import (ConsentFormUploadView, MedicalRecordCreateView,
                             MedicalRecordUpdateView, ProfileUpdateView,
                             SignUpView)

app_name = "players"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/update-profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('upload-medical-record/', MedicalRecordCreateView.as_view(), name='medical_record_add'),
    path('<int:pk>/edit-medical-record/', MedicalRecordUpdateView.as_view(), name='medical_record_edit'),
    path('<int:pk>/upload-consent-form/', ConsentFormUploadView.as_view(), name='consent_form_upload'),
]
