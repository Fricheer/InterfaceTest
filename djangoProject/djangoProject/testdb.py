# -*- coding: utf-8 -*-
import email
from os import name
from traceback import print_list
from django.db.models.query import RawQuerySet
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache  # 导入 Django 缓存模块
import sqlite3
import base64
import pickle
import datetime

from TestModel.models import Test,Blog,Author,Entry
import pymysql

# 数据库操作
def testdb(request):
    name = request.GET.get('name', 'runoob')  # 没有就用默认值
    age = request.GET.get('age', 18)          # 没有就用默认值
    email = request.GET.get('email', 'unknown@example.com')  # 没有就用默认值
    # 注意：GET获取到的都是字符串，age需要转成int
    test1 = Test(
        name=name,
        age=int(age),
        email=email
    )
    test1.save()

    # 将数据存入 Redis
    redis_key = f"user:{name}"
    user_data = {
        "name": name,
        "age": age,
        "email": email
    }
    cache.set(redis_key, user_data, timeout=3600)  # 数据保存 1 小时

    return HttpResponse(f"<p>数据添加成功！name={name}, age={age}, email={email}</p>")

def get_redis_data(request):
    name = request.GET.get('name', 'runoob')
    redis_key = f"user:{name}"
    user_data = cache.get(redis_key)
    if user_data:
        return HttpResponse(f"<p>从 Redis 获取数据成功！数据为：{user_data}</p>")
    else:
        return HttpResponse("<p>Redis 中未找到对应数据</p>")

def testdb01(request):
    #初始化
    response = ''
    response1 = ''
    #通过object这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()# type: ignore
    print(list)
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)# type: ignore

    # 获取单个对象
    response3 = Test.objects.get(id=1)# type: ignore

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4 = Test.objects.order_by("name")[0:2]# type: ignore

    #数据排序
    Test.objects.order_by("id")# type: ignore

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")# type: ignore

    # 输出所有数据
    for var in list:
        # print(var)
        response1 += f"{var.id}<br>"
    response = response1
    return HttpResponse("<p>" + response + "</p>")# type: ignore

def testdb_update(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    age  = request.GET.get('age')
    email = request.GET.get('email')
    if not id:
        return HttpResponse("<p>请提供id参数</p>")
    try:
        test1 = Test.objects.get(id=id)
    except Test.DoesNotExist:
        return HttpResponse("<p>id不存在</p>")
    if name:
        test1.name = name
    if age:
        test1.age = age
    if email:
        test1.email = email

    test1.save()
    return HttpResponse(f"<p> 修改成功，id={id} </p>")

def testdb_delete(request):
    test1 = Test.objects.get(id=1).delete()# type: ignore
    return HttpResponse("<p> 删除成功 <p>")# type: ignore

def insert_blog(request):
    b = Blog(name='shiping,zheng',tagline='添加一个name')
    b.save()
    return HttpResponse("<p> 插入数据成功 <p>")

def update_blog(request):
    b5 = Blog.objects.filter(name='shiping.zheng').first()
    b5.name = '张三'
    b5.save()
    return HttpResponse("<p> 修改数据成功 <p>")

def un(request):
    entry = Entry.objects.get(id=1)
    cheese_blog = Blog.objects.get(name="张三")
    entry.blog = cheese_blog
    entry.save()
    return HttpResponse("<p> 表关联成功 <p>")

def unadd(request):
    zero = Author.objects.create(name='zero')
    entry = Entry.objects.get(id = 1)
    entry.authors.add(zero)
    return HttpResponse("<p> 表关联成功 <p>")

def select_entry(request):
    entry = Entry.objects.all().values().filter(id=1)
    print(Entry.objects.filter(id=1))
    print(Entry.objects.all().values())
    return HttpResponse(entry)