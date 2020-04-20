from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    # 获取拼接参数
    url('get/(?P<year>\d{4})/(?P<address>[a-zA-Z]+)', views.get_all_params),
    url('^post', views.query),
    url('^form', views.get_form),
    url('not_form', views.get_not_form),
    url('other_params', views.get_others)
]