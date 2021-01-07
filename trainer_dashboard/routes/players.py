from django.urls import path

from ..views.players import PlayerListView

app_name = "players"

urlpatterns = [
    path('all/', PlayerListView.as_view(), name="players_list")
]