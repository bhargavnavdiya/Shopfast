from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method== 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken...')
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken...')
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken...')
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken...')
            return redirect('/')
        else:
            user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
            user.save();
            messages.info(request,'User created sucessfully...')
            return redirect('login')

        
    else:
        return render(request,'register.html')




def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')