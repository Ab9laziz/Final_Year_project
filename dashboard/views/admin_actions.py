from django.contrib import auth, messages
from django.shortcuts import get_object_or_404, redirect
from portal.models import Fixture, TrainingSession

from ..utils import send_activation_email, send_suspension_email

User = auth.get_user_model()

# logic for suspending users and redirection based on user type


def suspend_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()

    if(user.role == 'player'):
        send_suspension_email(user, request)
        messages.success(request, "Account Suspended")
        return redirect("dashboard:players:player_details", pk=pk)
    elif(user.role == 'trainer'):
        send_suspension_email(user, request)
        messages.success(request, "Account Suspended")
        return redirect("dashboard:trainers:trainer_details", pk=pk)
    # elif(user.role == 'instructor'):
    #     send_suspension_email(user, request)
    #     messages.success(request,"Account Suspended")
    #     return redirect("dashboard:instructor_details", pk=pk)

# logic for activating users and redirection


def activate_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = True
    user.save()

    if(user.role == 'player'):
        send_activation_email(user, request)
        messages.success(request, "Account activated")
        return redirect("dashboard:players:player_details", pk=pk)
    elif(user.role == 'trainer'):
        send_activation_email(user, request)
        messages.success(request, "Account activated")
        return redirect("dashboard:trainers:trainer_details", pk=pk)
    # elif(user.role == 'instructor'):
    #     messages.success(request,"Account activated")
    #     return redirect("dashboard:instructor_details", pk=pk)


def fixture_remove_player(request, pk, user_pk):
    fixture = Fixture.objects.get(id=pk)
    player = User.objects.get(id=user_pk)
    fixture.starting_players.remove(player)
    fixture.save()
    messages.success(request, "Player Removed from Starting Team")
    return redirect('dashboard:fixtures:fixture_details', pk=pk)


def fixture_remove_subtitute(request, pk, user_pk):
    fixture = Fixture.objects.get(id=pk)
    player = User.objects.get(id=user_pk)
    fixture.subtitutes.remove(player)
    fixture.save()
    messages.success(request, "Player Removed from List of Subtitutes")
    return redirect('dashboard:fixtures:fixture_details', pk=pk)


def training_remove_player(request, pk, user_pk):
    session = TrainingSession.objects.get(id=pk)
    player = User.objects.get(id=user_pk)
    session.players.remove(player)
    session.save()
    messages.success(request, "Player Removed from List of Players")
    return redirect('dashboard:sessions:session_details', pk=pk)


def training_remove_trainer(request, pk, user_pk):
    session = TrainingSession.objects.get(id=pk)
    trainer = User.objects.get(id=user_pk)
    session.trainers.remove(trainer)
    session.save()
    messages.success(
        request, "Trainer Removed from List of Trainers for this training session")
    return redirect('dashboard:sessions:session_details', pk=pk)
