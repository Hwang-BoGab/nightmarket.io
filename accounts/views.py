from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'username or passowrd is incorrect'})
    else:
        return render(request, 'login.html')

def join(request):
    if request.method == 'POST':
            if request.POST['pass'] == request.POST['repeat-pass']:
                user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
    return render(request, 'join.html')

def logout(requests):
    
    pass
