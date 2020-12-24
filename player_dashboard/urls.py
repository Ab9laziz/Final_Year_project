from django.urls import path, include

app_name = "player_dashboard"

urlpatterns = [
    path('', include('player_dashboard.routes.index'))
]
