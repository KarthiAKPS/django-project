from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials, Try again!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    
    if request.method == 'POST':
        username = request.POST['user_name']
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("user name already exists")
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("user email already exists")
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                usr = User.objects.create_user( username = username,email = email, password = password1, first_name=first_name, last_name=last_name)
                usr.save()
                return redirect('login')
        else:
            print('password not matching')
            messages.info(request,'password not matching')
            return redirect('register')
    
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')