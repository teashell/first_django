from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('attr', views.work),
    url('json',views.json),
    url('red', views.red)
]
