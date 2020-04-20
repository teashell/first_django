from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def set_cookie(request):
    print(request.COOKIES)
    res = HttpResponse()
    res.content = '我已经设置好了cookie!!!'
    res.status_code = 200
    res.set_cookie('name', value='lisi',max_age=30)
    return res

