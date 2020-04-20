from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls.base import reverse


# Create your views here.
def work(request):
    res = HttpResponse()
    res.content = '恭喜你,Django已经快搞完了!!'
    res.status_code = 200
    return res


def json(request):
    data_dict = {
        'name': 'zs',
        'age': 100
    }
    data_list = [
        {
            'name': 'lisi',
            'age': 200
        }
    ]
    res = JsonResponse(data_list,safe=False)
    return res


# 重定向
def red(request):
    # return redirect('/register/register')
    return redirect(reverse('redirect_register'))
