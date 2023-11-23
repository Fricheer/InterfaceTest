# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test


# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

def testdb01(request):
    #初始化
    response = ''
    response1 = ''
    #通过object这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4 = Test.objects.order_by("name")[0:2]

    #数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")

def testdb_update(request):
    test1 = Test.objects.get(id=1)
    test1.name = 'demo01'
    test1.save()

    return HttpResponse("<p> 修改成功 <p>")

def testdb_delete(request):
    test1 = Test.objects.get(id=1).delete()
    return HttpResponse("<p> 删除成功 <p>")