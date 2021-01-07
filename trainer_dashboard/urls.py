from django.urls import path, include

app_name = "trainer_dashboard"

urlpatterns = [
    path('', include('trainer_dashboard.routes.index')),
    path('fixtures/', include('trainer_dashboard.routes.fixtures')),
    path('training-sessions/', include('trainer_dashboard.routes.sessions')),
    path('players/', include('trainer_dashboard.routes.players')),
]
