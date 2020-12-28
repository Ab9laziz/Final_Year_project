from django.contrib import auth, messages
from django.shortcuts import redirect
from portal.models import TrainingSession

User = auth.get_user_model()


def training_remove_player(request, pk, user_pk):
    session = TrainingSession.objects.get(id=pk)
    player = User.objects.get(id=user_pk)
    session.players.remove(player)
    session.save()
    messages.success(request, "Player Removed from List of Players")
    return redirect('trainer_dashboard:sessions:session_details', pk=pk)


def training_remove_trainer(request, pk, user_pk):
    session = TrainingSession.objects.get(id=pk)
    trainer = User.objects.get(id=user_pk)
    session.trainers.remove(trainer)
    session.save()
    messages.success(
        request, "Trainer Removed from List of Trainers for this training session")
    return redirect('trainer_dashboard:sessions:session_details', pk=pk)
