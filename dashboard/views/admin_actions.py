from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

# logic for suspending users and redirection based on user type
def suspend_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()

    if(user.role == 'player'):
        messages.success(request,"Account Suspended")
        return redirect("dashboard:players:player_details", pk=pk)
    elif(user.role == 'trainer'):
        messages.success(request,"Account Suspended")
        return redirect("dashboard:trainers:trainer_details", pk=pk)
    # elif(user.role == 'instructor'):
    #     messages.success(request,"Account Suspended")
    #     return redirect("dashboard:instructor_details", pk=pk)

# logic for activating users and redirection
def activate_user(request,pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = True
    user.save()

    if(user.role == 'player'):
        messages.success(request,"Account activated")
        return redirect("dashboard:players:player_details", pk=pk)
    elif(user.role == 'trainer'):
        messages.success(request,"Account activated")
        return redirect("dashboard:trainers:trainer_details", pk=pk)
    # elif(user.role == 'instructor'):
    #     messages.success(request,"Account activated")
    #     return redirect("dashboard:instructor_details", pk=pk)