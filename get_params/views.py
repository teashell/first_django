from django.shortcuts import render
from django.http.response import HttpResponse
import json


# Create your views here.
def get_all_params(request, address, year):
    return HttpResponse('year:'+year + 'address:'+address)


def query(request):
    print('查询参数为:', request.GET)
    # 参数解析
    result = request.GET
    keys = request.GET.keys()
    for i in keys:
        print(f'查询参数{i}的值是{result.getlist(i)}')

    return HttpResponse('已经成功获取所有的查询参数!!!')


def get_form(request):
    print(request.POST)
    return HttpResponse('form表单的数据已经获取完了!!')


def get_not_form(request):
    print(request.body)
    json_str = request.body.decode('utf8')
    print(json_str)
    print(type(json_str))
    my_dict = json.loads(json_str)
    print(my_dict)
    print(type(my_dict))

    return HttpResponse('非form表单的数据已经获取完了')


def get_others(request):
    # 请求头信息:
    head = request.META
    print(head['USERNAME'])
    # 方法
    print(request.method)
    # 用户对象
    print(request.user)
    # 请求页面的完整路径
    print(request.path)
    return HttpResponse('获取到所有的其他莫名其妙的参数!!!')
