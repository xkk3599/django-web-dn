from django.http import HttpResponse
from django.template import loader
from django.shortcuts import  render


def page_2003_view(request):
    html = '这是index页面'
    return HttpResponse(html)

def index_view(request):
    html='这是index页面'
    return HttpResponse(html)

def page1_view(request):
    html = '这是page1页面'
    return HttpResponse(html)

def page2_view(request):
    html = '这是page2页面'
    return HttpResponse(html)

def pagen_view(request,pg):
    html = '这是page%s页面!!!!'%(pg)
    return HttpResponse(html)

def cal_view(request,n,op,m):
    if op not in ['add','sub','mul']:
        return HttpResponse('Your op is Wrong')
    result=0
    if op=='add':
        return HttpResponse(n+m)
    elif op =='sub':
        return HttpResponse(n-m)
    else:
        return HttpResponse(n*m)

def cal2_view(request,x,op,y):
    if op not in ['add','sub','mul']:
        return HttpResponse('Your op is Wrong')
    result=0
    if op=='add':
        return HttpResponse(x+y)
    elif op =='sub':
        return HttpResponse(x-y)
    else:
        return HttpResponse(x*y)

#1.通过loader加载模板
# t=loader.get_template("模板文件名")
#2.将t转换成html字符串
# html=t.render(字典数据)

def fun1():
    print("hello")
    return 444
def test_html(request):
    # t=loader.get_template('test_html.html')
    # html=t.render
    # return HttpResponse(html)

    #方案二：

    #render(request,'test_html.html',dict)#第三个参数是字典，用来变量交互
    dic={'username':'kkk','age':18,'fun1':fun1}#fun1 传递函数和对象都可以
    return render(request,'test_html.html',dic)

def test_mycal(request):
    if request.method=='GET':
        return render(request,'test_html.html')
    elif request.method=='POST':
        x=request.Post['x']
        y = request.Post['y']
        op = request.Post['op']

        # dic={}
        return render(request,'test_html.html',locals())