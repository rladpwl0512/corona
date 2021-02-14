from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else: 
            messages.info(request, '로그인에 실패하였습니다.')
    return render(request, 'accounts/signin.html')
    

def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists(): #아이디 중복 체크 
            messages.info(request, '이미 존재하는 아이디입니다.')
        elif request.POST['password1'] != request.POST['password2']:
            messages.info(request, '비밀번호가 다릅니다.')
        elif request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('main')
    return render(request, 'accounts/signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main') #로그아웃이 제대로 되면 main으로 
    return render(request, 'accounts/signin.html')



