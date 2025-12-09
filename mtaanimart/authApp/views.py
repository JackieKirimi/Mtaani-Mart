from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from ProductApp.models import CartItem
from .forms import CheckoutForm
from django.conf import settings
from django import forms
#from django.core.serializers import serialize
#from .models import DeliveryPoint


def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '254742252718'
    amount = 1
    account_reference = 'Mtaani mart'
    transaction_desc = 'product purchase'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

@login_required(login_url='login')
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    amount = int(total) if total >= 1 else 1
    quantities = range(1, 11)

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            quantity = int(request.POST.get("quantity", 1))

            
            if cart_items.exists():
                product_price = cart_items.first().product.price
                total = product_price * quantity
                amount = int(total)

            cl = MpesaClient()
            account_reference = "Mtaani Mart"
            transaction_desc = "Pickup at Mtaani Mart Shop"
            callback_url = "https://api.darajambili.com/express-payment"

            response = cl.stk_push(
                phone_number, amount,
                account_reference, transaction_desc,
                callback_url
            )
            print(response)
            return HttpResponse(response)
    else:
        form = CheckoutForm()

    return render(request, "authApp/checkout.html", {
        "form": form,
        "cart_items": cart_items,
        "total": total,
        "quantities": quantities,
    })

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

def mpesaPayment(request):
    
    
    context={}
    return render(request,'authApp/prompt_stk_push.html',context)

@login_required(login_url='login')  
def help_page(request):
    return render(request, "authApp/help.html")





'''def delivery_points_map(request):
    points = DeliveryPoint.objects.all()
    points_json = serialize('geojson', points)
    return render(request, 'delivery_map.html', {'delivery_points': points_json})'''


