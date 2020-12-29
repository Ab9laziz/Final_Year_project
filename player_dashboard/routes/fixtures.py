from django.urls import path

from ..views.fixtures import FixtureDetailView, FixtureListView

app_name = "fixtures"

urlpatterns = [
    path('all/', FixtureListView.as_view(), name="fixtures_list"),
    path('<int:pk>/details/', FixtureDetailView.as_view(), name="fixture_details"),
]
