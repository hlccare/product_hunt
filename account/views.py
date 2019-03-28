from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        # return redirect('/')
        user_name = request.POST['用户名']
        password1 = request.POST['密码']
        password2 = request.POST['确认密码']
        try:
            User.objects.get(username=user_name)

            return render(request,'signup.html',{'错误信息':'该用户名已存在'})
        except User.DoesNotExist:
            if password1 and password1 == password2:
                User.objects.create_user(username=user_name, password=password1)
                return redirect('主页')
            else:
                return render(request, 'signup.html', {'密码错误信息':'两次输入密码不一致'})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        pass_word = request.POST['密码']
        #鉴定用户，存在的话返回一个用户，否则返回NONE
        # user = auth.authenticate(username=user_name, pass_word=pass_word)
        try:
            user = User.objects.get(username=user_name)
            pwd = user.password
            # if user:
            if check_password(pass_word, pwd):
                auth.login(request, user)
                return redirect('主页')
            else:
                return render(request, 'login.html', {'错误信息':'用户名或密码错误'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'错误信息': '用户名或密码错误'})

def logout(request):
    auth.logout(request)
    return redirect('主页')