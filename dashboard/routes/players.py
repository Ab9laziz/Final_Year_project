from django.urls import path

from ..views.players import PlayerDetailView, PlayerListView, PlayerSuspendView

app_name = "players"

urlpatterns = [
    path('all/', PlayerListView.as_view(), name='players_list'),
    path('<int:pk>/details', PlayerDetailView.as_view(), name='player_details'),
    path('<int:pk>/suspend', PlayerSuspendView.as_view(), name='player_confirm_suspend'),
]
