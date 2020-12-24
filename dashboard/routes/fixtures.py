from django.urls import path

from ..views.admin_actions import (fixture_remove_player,
                                   fixture_remove_subtitute)
from ..views.fixtures import (FixtureAddPlayersView, FixtureAddSubtitutesView,
                              FixtureCreateView, FixtureDetailView,
                              FixtureListView, FixtureUpdateView, FixtureEditPlayersView, FixtureEditSubtitutesView)

app_name = "fixtures"

urlpatterns = [
    path('all/', FixtureListView.as_view(), name="fixtures_list"),
    path('add/', FixtureCreateView.as_view(), name="fixture_add"),
    path('<int:pk>/details', FixtureDetailView.as_view(), name="fixture_details"),
    path('<int:pk>/edit', FixtureUpdateView.as_view(), name="fixture_edit"),
    path('<int:pk>/select-starting-players/',
         FixtureAddPlayersView.as_view(), name="fixture_add_players"),
    path('<int:pk>/select-subtitutes/',
         FixtureAddSubtitutesView.as_view(), name="fixture_add_subs"),
     path('<int:pk>/add-players/',
         FixtureEditPlayersView.as_view(), name="fixture_edit_players"),
     path('<int:pk>/add-subtitutes/',
         FixtureEditSubtitutesView.as_view(), name="fixture_edit_subs"),

    # admin actions
    path('<int:pk>/remove-player/<int:user_pk>/',
         fixture_remove_player, name="fixture_remove_player_action"),
    path('<int:pk>/remove-subtitute/<int:user_pk>/',
         fixture_remove_subtitute, name="fixture_remove_sub_action"),

]
