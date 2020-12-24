from django.urls import path

from ..views.fixtures import FixtureAddPlayersAPIView, FixtureAddSubtitutesAPIView

app_name = "fixtures_api"

urlpatterns = [
    path('fixtures/add-players/', FixtureAddPlayersAPIView.as_view(), name="fixture_player_actions"),
    path('fixtures/add-subtitutes/', FixtureAddSubtitutesAPIView.as_view(), name="fixture_sub_actions"),
]
