
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from payment.views import lipa
from home.views import IndexTemplateView
from users.views.base import UserAccountTemplateView, logout_user, login_redirect, LoginUserView


urlpatterns = [
    # index page url
    path('',IndexTemplateView.as_view(), name="index"),

    # authentication urls
    path('accounts/', include('allauth.urls')),
    path('accounts/logout', logout_user, name='logout'),
    path('accounts/login/', LoginUserView.as_view(), name='account_login'),
    path('accounts/login-redirect/', login_redirect, name='login_redirect'),

    # app urls
    path('players/', include('users.urls.players', namespace='players')),
    path('lipa', lipa , name= 'lipa'),
    path('portal/',include('portal.urls')),

    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
