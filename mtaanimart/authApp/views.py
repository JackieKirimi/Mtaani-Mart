from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
 

# Create your views here.
def loginUser(request):
    if request.method=='POST':
        username =request.POST.get('username').lower()
        password =request.POST.get('password')
        try:
            user= User.objects.get(username=username)
        except:
            print('User not found') #flash message
        user= authenticate(request, username=username,password=password)
        
        if user is not None:
            login(request ,user)
            return redirect('home')
        else:
            print('Wrong Credentials') 
    context={}
    return render(request, 'authApp/login_form.html', context)

def logoutUser(request):
    context={}
    logout(request)
    return redirect('login')

def registerUser(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
          user=form.save(commit=False)
          user.username=user.username.lower()
          user.save()
          login(request,user)
          return redirect('home')
    
    context={"form": form}
    return render(request, 'authApp/register_form.html', context)