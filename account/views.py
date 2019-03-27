from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
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