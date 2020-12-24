from django.urls import path, include

app_name = "trainer_dashboard"

urlpatterns = [
    path('', include('trainer_dashboard.routes.index'))
]
