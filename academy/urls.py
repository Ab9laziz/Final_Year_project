
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
from payment.views import lipa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('lipa', lipa , name= 'lipa'),
    path('portal/',include('portal.urls')),
]
