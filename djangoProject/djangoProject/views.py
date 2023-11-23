from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request,'Form_02.html')