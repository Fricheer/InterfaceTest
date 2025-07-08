from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
import json
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def runoobs(request):
    # if not request.user.is_authenticated:
    #     return JsonResponse({'error': '未登录'}, status=401)
    views_list = ['菜鸟教程01','菜鸟教程02','菜鸟教程03']
    views_dict = {"age":18,"income":20000}
    name = "<a href='https://www.runoob.com/'>点击跳转</a>"
    import datetime
    import random
    now = datetime.datetime.now()
    num = random.randint(1,100)
    return render(request, 'runoob.html', {'views_list': views_list,"now":now,"num":num,"name":name,"views_dict":views_dict})


class RunoobsView(APIView):
    def get(self, request):
        views_list = ['菜鸟教程01','菜鸟教程02','菜鸟教程03']
        views_dict = {"age":18,"income":20000}
        name = "<a href='https://www.runoob.com/'>点击跳转</a>"
        import datetime
        import random
        now = datetime.datetime.now()
        num = random.randint(1,100) 
        return Response({'views_list': views_list, "now": now, "num": num, "name": name, "views_dict": views_dict})
    
# @csrf_exempt
# @require_POST
def json01(request):
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return JsonResponse(data)

def json02(request):
    return redirect('json01')

def set_session(request):
    # 设置 session
    request.session['username'] = '张三'
    username = request.session.get('username', '未登录')
    return JsonResponse({'username': username})

def get_all_session(request):
    session_data = dict(request.session.items())
    return JsonResponse({'session': session_data})

def show_session(request):
    username = request.session.get('username', '未登录')
    return render(request, 'your_template.html', {'username': username})

def clear_session(request):
    """清除session"""
    request.session.clear()
    return JsonResponse({'msg': 'session已清除'})

from django.http import JsonResponse

def clear_all_session(request):
    request.session.flush()  # 清除服务端session并让sessionid失效
    response = JsonResponse({'msg': 'session已清除'})
    response.delete_cookie('sessionid')  # 删除客户端cookie
    return response

@csrf_exempt  # 测试用，生产建议用csrf token
def set_post_session(request):
    if request.method == 'POST':
        # 获取json数据
        data = json.loads(request.body)
        username = data.get('username', '未提供')
        request.session['username'] = username
        return JsonResponse({'msg': f'session已设置为{username}'})
        response['']
    else:
        return JsonResponse({'error': '只支持POST'}, status=405)


