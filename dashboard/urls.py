from django.urls import path, include

app_name = "dashboard"

urlpatterns = [
    path('', include('dashboard.routes.index')),
    path('players/', include('dashboard.routes.players')),
    path('trainers/', include('dashboard.routes.trainers')),
    path('fixtures/', include('dashboard.routes.fixtures')),
]


