from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def set_my_session(request):
    # 设置session
    # request.session['name'] = 'heima'
    request.session['age'] = 100
    request.session['gender'] = '男'
    return HttpResponse(content='已经设置好了session!!!', status=200)


def get_my_session(request):
    print(request.session['name'])
    print(request.session['age'])
    print(request.session['gender'])
    return HttpResponse('已经获取到了你的session值哦!!!')


def del_my_session(request):
    # 删除单个值
    # del request.session['age']
    # 删除redis中值
    # request.session.clear()
    # 删除整条redis记录
    request.session.flush()
    return HttpResponse('已经删除了你不想要的cookie!!!')

