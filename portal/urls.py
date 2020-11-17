from django.conf.urls import url
from . import views

app_name='portal'

urlpatterns = [
    #/home/
    url(r'^$',views.Index,name='index'),

]