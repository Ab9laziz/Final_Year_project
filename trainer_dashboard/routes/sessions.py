from django.urls import path

from ..views.sessions import (TrainingSessionAddPlayersView,
                              TrainingSessionAddTrainersView,
                              TrainingSessionCreateView,
                              TrainingSessionDetailView,
                              TrainingSessionEditPlayersView,
                              TrainingSessionEditTrainersView,
                              TrainingSessionListView,
                              TrainingSessionUpdateView)
from ..views.trainer_actions import (training_remove_player,
                                     training_remove_trainer)

app_name = "sessions"

urlpatterns = [
    path('all/', TrainingSessionListView.as_view(), name="sessions_list"),
    path('add/', TrainingSessionCreateView.as_view(), name="session_add"),
    path('<int:pk>/details', TrainingSessionDetailView.as_view(),
         name="session_details"),
    path('<int:pk>/edit', TrainingSessionUpdateView.as_view(), name="session_edit"),
    path('<int:pk>/select-players/',
         TrainingSessionAddPlayersView.as_view(), name="session_add_players"),
    path('<int:pk>/select-trainers/',
         TrainingSessionAddTrainersView.as_view(), name="session_add_trainers"),
    path('<int:pk>/add-players/',
         TrainingSessionEditPlayersView.as_view(), name="session_edit_players"),
    path('<int:pk>/add-trainers/',
         TrainingSessionEditTrainersView.as_view(), name="session_edit_trainers"),

    # admin actions
    path('<int:pk>/remove-player/<int:user_pk>/',
         training_remove_player, name="session_remove_player_action"),
    path('<int:pk>/remove-Trainer/<int:user_pk>/',
         training_remove_trainer, name="session_remove_trainer_action"),

]
