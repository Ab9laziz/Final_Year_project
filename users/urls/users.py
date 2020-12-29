from django.urls import path
from ..views.base import UserDetailView, UserProfileUpdateView, UserProfileUpdateView

app_name = "users"

urlpatterns = [
    path('my-profile/', UserDetailView.as_view(), name="user_profile"),
    path('<int:pk>/profile-update/',
         UserProfileUpdateView.as_view(), name="profile_update"),
]
