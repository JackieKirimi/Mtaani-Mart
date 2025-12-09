from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from .models import Product, CartItem



def home(request):
    return render(request, 'ProductApp/home.html')

@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect("product_list")  
    else:
        form = ProductForm()

    context = {
        "products": products,
        "form": form,
    }
    return render(request, "ProductApp/product_list.html", context)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = ProductForm()
    
    return render(request, 'productApp/add_product.html', {'form': form})

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


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={"quantity": 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart")

@login_required(login_url='login')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'ProductApp/cart.html', {"cart_items": cart_items, "total": total})
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect("cart")

