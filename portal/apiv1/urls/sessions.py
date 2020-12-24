from django.urls import path

from ..views.sessions import TrainingAddPlayersAPIView, TrainingAddTrainersAPIView

app_name = "sessions_api"

urlpatterns = [
    path('sessions/add-players/', TrainingAddPlayersAPIView.as_view(), name="session_player_actions"),
    path('sessions/add-subtitutes/', TrainingAddTrainersAPIView.as_view(), name="session_trainer_actions"),
]
