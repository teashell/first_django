from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('register', views.register),
    url('register/$',views.register, name='redirect_register'),
]