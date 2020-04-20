from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('set', views.set_cookie)
]
