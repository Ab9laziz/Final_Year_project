from django.urls import path

from ..views.fixtures import (FixtureCreateView, FixtureDetailView,
                              FixtureListView, FixtureUpdateView)

app_name = "fixtures"

urlpatterns = [
    path('all/', FixtureListView.as_view(), name="fixtures_list"),
    path('add/', FixtureCreateView.as_view(), name="fixture_add"),
    path('<int:pk>/details', FixtureDetailView.as_view(), name="fixture_details"),
    path('<int:pk>/edit', FixtureUpdateView.as_view(), name="fixture_edit"),
]
