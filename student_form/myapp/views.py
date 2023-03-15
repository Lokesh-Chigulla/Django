from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout, get_user_model
from myapp.models import Form

# Create your views here.

def index(request):
    return render(request,'home.html')



def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password1 = request.POST['password1']

        user=authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
        
    return render(request, 'login.html')



def signup(request):
    if request.method=='POST': 
        first_name=request.POST['first_name']
        email=request.POST['email']
        username=request.POST['username']
        password1 = request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User taken')
                return redirect('signup')
            elif User.objects.filter(email=email):
                messages.info(request, 'Email-id taken')
                return redirect('signup')
            else:                
                user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name)
                user.save()
                messages.info(request, ' Account Created')
                return redirect('signup')
        else:
            messages.info(request, 'Password is not Matching')
            return redirect('signup') 
        return redirect('login')
    return render(request, 'signup.html')

def main(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        college=request.POST.get('college')
        email=request.POST.get('email')
        phone=request.POST.get('phone')

        main=Form.objects.create(firstname=firstname, lastname=lastname, gender=gender, college=college, email=email, phone=phone)
        main.save()
        print('Created')
    return render(request, 'main.html')