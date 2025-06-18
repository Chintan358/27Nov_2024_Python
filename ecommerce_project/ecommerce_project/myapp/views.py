from django.shortcuts import render,HttpResponse,redirect

from myapp.models import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
        request.session['cart_count'] = cart_count
    else:
        request.session['cart_count'] = 0
   
    context = {
        'products': products,
        'categories': categories,
        'title': 'Home',
        'cart_count': request.session['cart_count']
    }
    return render(request,"index.html", context)

@login_required(login_url='login')
def cart(request):
    
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)

    return render(request,"cart.html", {'cart_items': cart_items, 'title': 'Cart', 'total_price': total_price})

def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,"contact.html", {'title': 'Contact Us'})

def detail(request):
    return render(request,"detail.html")

def shop(request):
    return render(request,"shop.html", {'title': 'Shop'})


def getProdducts(request):

    category = request.GET.get('categories')
    print("Category:", category)
    price = request.GET.get('price', None)
    if category:
        all_products = Product.objects.filter(category__categoryname=  y)
    elif price:
        all_products = Product.objects.filter(price__lte=price)
    else:
        all_products = Product.objects.all()
    return JsonResponse({"products": list(all_products.values())})

def getCategories(request):
    all_categories = Category.objects.all()
    return JsonResponse({"categories": list(all_categories.values())})


def register_page(request):
    if request.method == 'POST':
        # Handle registration logic here
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # You would typically save the user to the database here

        user  = User(
            first_name=first_name,
            last_name=last_name,
            username=username,        
        )
        user.set_password(password)
        user.save()
        return render(request, "register.html", {'title': 'Register', 'message': 'Registration successful! Please log in.'})
    return render(request, "register.html", {'title': 'Register'})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index page after login
        else:
            return render(request, "login.html", {'title': 'Login', 'error': 'Invalid credentials'})
    return render(request, "login.html", {'title': 'Login'})


def logout_page(request):
    logout(request)
    return redirect('index')  # Redirect to the index page after logout


def add_to_cart(request):
    
    if request.user.is_anonymous:
        return HttpResponse(request.user)
    else :
        product_id = request.GET.get('product_id')
        product = Product.objects.get(id=product_id)

        cart = Cart.objects.filter(user=request.user, product=product).exists()
        if cart:
            return HttpResponse("Product already in cart")
       
        cart = Cart.objects.create(
            user=request.user,
            product=product,
            qty=1  # Default quantity is set to 1
        )
        return HttpResponse(f"Product added to cart successfully: {product.productname}")
    

def change_cart_item_qty(request):
    
    
    cart_item_id = request.GET.get('item_id')
    new_qty = int(request.GET.get('change'))  # Default to 1 if not provided

    try:
        cart_item = Cart.objects.get(id=cart_item_id, user=request.user)
        cart_item.qty = cart_item.qty+ new_qty  # Update the quantity by adding the new_qty
        if cart_item.qty <= 0:
            cart_item.delete()  # Remove item if quantity is zero or less
            return HttpResponse("Cart item removed due to zero quantity")
        cart_item.save()
        return HttpResponse(f"Cart item quantity updated to {new_qty}")
    except Cart.DoesNotExist:
        return HttpResponse("Cart item not found")

def remove_cart_item(request):
    cart_item_id = request.GET.get('item_id')

    try:
        cart_item = Cart.objects.get(id=cart_item_id, user=request.user)
        cart_item.delete()  # Remove the item from the cart
        return HttpResponse("Cart item removed successfully")
    except Cart.DoesNotExist:
        return HttpResponse("Cart item not found")