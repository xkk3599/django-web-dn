"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from . import views
urlpatterns = [# 在setting中的变量，找到urls文件，和这个变量.
    path('admin/', admin.site.urls),#路由函数
    #http://127.0.0.1:8000/page/2003
    path('page/2003/',views.page_2003_view),#arg0：path地址，arg2：视图函数的引用，不要加括号
    path('',views.index_view),
    path('page/1',views.page1_view),
    path('page/2',views.page2_view),
    #path转换器，将匹配到的页面，参数传给视图函数。关键字传参
    # path('page/<int:args>',views.xx) xx的args。
    # path('page/<str:args>',views.xx) xx的args。
    path('page/<int:pg>',views.pagen_view),
    #re_path  匹配的更精确。
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})',views.cal2_view),#参数x,op,y传递
    # path('<int:n>/<str:op>/<int:m>',views.cal_view)
    path('test_html',views.test_html)

]
