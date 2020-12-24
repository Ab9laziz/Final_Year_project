from django.conf.urls import url
from django.urls import path, include
from . import views

app_name='portal'

urlpatterns = [
    #/home/
    path('portal/',views.Index,name='index'),
    path('api/v1/', include('portal.apiv1.urls.fixtures')),
    path('api/v1/', include('portal.apiv1.urls.sessions'))

]