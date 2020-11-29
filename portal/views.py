from django.shortcuts import render



def Index(request):
    return render(request,'users/players/sidebar.html')