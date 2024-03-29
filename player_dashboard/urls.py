from django.urls import path, include

app_name = "player_dashboard"

urlpatterns = [
    path('', include('player_dashboard.routes.index')),
    path('fixtures/', include('player_dashboard.routes.fixtures')),
    path('payments/', include('player_dashboard.routes.payments')),
    path('training-sessions/', include('player_dashboard.routes.sessions')),
]
