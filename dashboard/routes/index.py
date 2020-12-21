from django.urls import path

from ..views.admin_actions import activate_user, suspend_user
from ..views.index import (ConsentFormCreateView, ConsentFormDetailView,
                           ConsentFormListView, ConsentFormUpdateView,
                           DashboardTemplateView, UserConfirmSuspendView)

app_name = "index"

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='index'),
    path('users/<int:pk>/confirm-deactivation',
         UserConfirmSuspendView.as_view(), name="user_confirm_suspension"),
    path('users/<int:pk>/suspend_user', suspend_user, name="user_suspend_action"),
    path('users/<int:pk>/unsuspend_user',
         activate_user, name="user_unsuspend_action"),

    # consent form urls
    path('consent-forms/all', ConsentFormListView.as_view(),
         name='consent_forms_list'),
    path('consent-forms/add', ConsentFormCreateView.as_view(),
         name='consent_form_add'),
    path('consent-forms/<int:pk>/details',
         ConsentFormDetailView.as_view(), name='consent_form_details'),
    path('consent-forms/<int:pk>/edit',
         ConsentFormUpdateView.as_view(), name='consent_form_edit'),
]
