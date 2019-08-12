from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
"""def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['pass']

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('home') # 로그인 성공시 홈페이지로 직접(redirect) 연결

            else:
                return render(request, 'login.html', {'error': 'username or passowrd is incorrect'}) # 로그인 실패시 { error message와 함께 } login페이지로 연결

    else:
        return render(request, 'login.html')
"""

def join(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method == 'POST':
            if request.POST['pass'] == request.POST['repeat-pass']:
                user = User.objects.create_user( 
                    #fullname=request.POST['fullname'],
                    request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['pass'],
                    #phone=request.POST['phone']
                ) 

                #auth.login(request, user) # 회원가입과 동시에 user 로그인

                return redirect('home') # 홈(home) 페이지로 직접(redircet) 연결

            
    # request.method != 'POST' (메소드 감지 X) -> 회원가입(join.html) 페이지로 연결
    else:
        return render(request, 'join.html') 


def logout(request):
    if request.method =='POST':
        auth.logout(request);
        return redirect('home')
    else:
        return render(request, 'join.html')

def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])

            if user is not None:
                auth.login(request, user)
                return redirect('home')

            else:
                return render(request, 'login_page.html', {'error': 'email or passowrd is incorrect'})

    else:
        return render(request, 'login_page.html')
