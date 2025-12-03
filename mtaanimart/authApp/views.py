from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
 

# Create your views here.
def loginUser(request):
    if request.method=='POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        try:
            user= User.objects.get(username=username)
        except:
            print('User not found') #flash message
        user= authenticate(request, username=username,password=password)
        
        if user is not None:
            login(request ,user)
            redirect('home')
        else:
            print('Wrong Credentials')
            
        
    context={}
    
    return render(request, 'authApp/login_form.html', context)

def logoutUser(request):
    context={}
    return render(request, 'authApp/login_form.html', context)

def registerUser(request):
    context={}
    return render(request, 'authApp/register_form.html', context)