from django.urls import path
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

]
