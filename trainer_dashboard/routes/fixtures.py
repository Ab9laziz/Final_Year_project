from django.urls import path
from ..views.fixtures import FixtureListView, FixtureDetailView

app_name = "fixtures"

urlpatterns = [
    path('all/', FixtureListView.as_view(), name="fixtures_list"),
    path('<int:pk>/details/', FixtureDetailView.as_view(), name="fixture_details"),
]
