from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def register(request):

    return HttpResponse('注册成功,转向登录界面!!')
