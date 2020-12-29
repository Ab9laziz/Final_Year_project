from django.urls import path

from ..views.sessions import TrainingSessionDetailView, TrainingSessionListView

app_name = "sessions"

urlpatterns = [
    path('all/', TrainingSessionListView.as_view(), name="sessions_list"),
    path('<int:pk>/details/', TrainingSessionDetailView.as_view(), name="session_details"),
]
