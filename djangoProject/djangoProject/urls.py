"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path as url
from django.urls import path,include
from . import views
from . import testdb,search
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('runoob/', views.runoob),
    path('Form03/',views.Form03),
    path('testdb/',testdb.testdb),
    path('testdb01/',testdb.testdb01),
    path('testdb02/', testdb.testdb_delete),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search_get),
    url(r'^search-post/$',search.search_post),
    path('login/', views.Login),
    path('Form/',views.Form),
    path('Javascripts/',views.JavaScripts),
    path('Jquery01/', views.Jquery),
    path('app01/', include('app01.urls')),
    path('accounts/', views.my_login_view),
]
