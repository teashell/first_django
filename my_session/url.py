from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('set', views.set_my_session),
    url('get', views.get_my_session),
    url('del', views.del_my_session)
]
