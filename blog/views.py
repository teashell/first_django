from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Hello World,这是第一个Django程序')


def login(request):
    return HttpResponse('登录失败,10000分钟后再登录!!!')

