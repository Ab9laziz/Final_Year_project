from django.urls import path

from ..views.trainers import TrainerCreateView, TrainerDetailView, TrainerListView

app_name = "trainers"

urlpatterns = [
    path('all/', TrainerListView.as_view(), name='trainers_list'),
    path('add/', TrainerCreateView.as_view(), name='trainer_add'),
    path('<int:pk>/details/', TrainerDetailView.as_view(), name='trainer_details'),
]