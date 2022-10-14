from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username=username, password=password)
            return redirect('users:login')
        else:
            return HttpResponse('비밀번호 확인 틀렸습니다.')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate가 있는지 없는지 확인해 주는 역활
        user = authenticate(request, username=username, password=password)
        if user:
            # login이 세션을 만들어주는 역활
            login(request, user)
            return redirect('users:user')
        else:
            return render(request,'login.html', {'error':'username or password is incorrect'})

def user(request):
    print(request.user)
    return render(request, 'user.html')

def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        "user": user
    }
    return render(request, 'profile.html',context)
    