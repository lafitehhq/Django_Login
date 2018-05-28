from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from . import models


def index(request):
    pass
    return render(request, 'login/index.html')

# 版本1
# def login(request):
#     #  情况1：使用Post方法提交的表单
#     if request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         message = '所有的字段都需要填写!'
#         # 情况1.1：账户密码都已经输入
#         if username and password:
#             username = username.strip()
#             # 情况1.1.1 判断账户
#             try:
#                 user = models.User.objects.get(name=username)
#             except:
#                 # 用户不存在直接跳转回login.html
#                 message = '用户不存在!'
#                 return render(request, 'login/login.html')
#             # 情况1.1.2 判断密码
#             if user.password == password:
#                 return redirect('/index/')
#             else:
#                 # 密码不正确直接跳转回login.html
#                 message = '密码错误!'
#                 return render(request, 'login/login.html')
#     #  情况1.2：账户密码都没有输入--直接跳转回login.html
#         else:
#             return render(request, 'login/login.html')
#     #  情况2：使用非Post方法提交的表单--直接跳转回login.html
#     else:
#         return render(request, 'login/login.html')


# 版本2
from . import forms  # 步骤一
def login(request):
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)  # 步骤二
        message = '所有的字段都需要填写!'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')  # 步骤三
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(name=username)
            except:
            # 用户不存在直接跳转回login.html
                message = '用户不存在!'
                return render(request, 'login/login.html', {'message': message})
            # 情况1.1.2 判断密码
            if user.password == password:
                return redirect('/index/')
            else:
                # 密码不正确直接跳转回login.html
                message = '密码错误!'
                return render(request, 'login/login.html', {'message': message})
            #  情况1.2：账户密码都没有输入--直接跳转回login.html
        else:
            return render(request, 'login/login.html', {'message': message})
    else:
        return render(request, 'login/login.html', locals())

def register(request):
    pass
    return render(request, 'login/register.html')

def logout(request):
    pass
    return redirect('/index/')  # 登出重定向到index界面






