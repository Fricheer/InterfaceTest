from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [

    path('hello/', views.runoobs),
    path('json01/', views.json01, name='json01'),
    path('json02/', views.json02),
    path('get_all_session/', views.get_all_session),
    path('show_session/', views.show_session),
    path('set_session/', views.set_session),
    path('clear_session/', views.clear_session),
    path('clear_all_session/', views.clear_all_session),   
    path('runoobs/', views.RunoobsView.as_view()),
    # 你可以继续添加其他路由
]