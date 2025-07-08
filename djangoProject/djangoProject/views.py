from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json


def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
#     # context          = {}
#     # context['hello'] = 'Hello World!'
    views_list = ['菜鸟教程01','菜鸟教程02','菜鸟教程03']
    views_dict = {"age":18,"income":20000}
    name = "<a href='https://www.runoob.com/'>点击跳转</a>"
    import datetime
    import random
    now = datetime.datetime.now()
    num = random.randint(1,100)
    return render(request, 'runoob.html', {'views_list': views_list,"now":now,"num":num,"name":name,"views_dict":views_dict})

def Form(request):
    return render(request,'Form.html')

def Form03(request):
    return render(request,'Form_03.html')
def Login(request):
    return render(request,'login.html')

def JavaScripts(request):
    return render(request,'Javascript.html')

def Jquery(request):
    return render(request,'Jquery01.html')

@csrf_exempt
def my_login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 这一步才是真正登录
            return JsonResponse({'msg': '登录成功'})
        else:
            return JsonResponse({'msg': '用户名或密码错误'}, status=400)
    else:
        return JsonResponse({'msg': '无效的请求方法'}, status=405)