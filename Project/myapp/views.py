from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import JsonResponse
import razorpay
# Create your views here.
def index(request):

    cid=0
    if request.method=="GET":
        data  =request.GET
        
        if(len(data)!=0):   
            print("hello")
            cid = data.get("cid")
    
    allcategories = Category.objects.all()
    if(cid):
        cat = Category.objects.filter(pk=cid)
        allproducts = Product.objects.filter(category=cid)
    else :
        allproducts = Product.objects.all()
    return render(request,"index.html",{"categories":allcategories,"products":allproducts})

@login_required(login_url="loginregister")
def accounts(request):
    return render(request,"accounts.html")

@login_required(login_url="loginregister")
def cart(request):
    cartdata = Cart.objects.filter(user=request.user)

    sum = 0
    for cart in cartdata:
        sum += cart.qty*cart.product.price

    return render(request,"cart.html",{"carts":cartdata,"total":sum})

@login_required(login_url="loginregister")
def checkout(request):
    cartdata = Cart.objects.filter(user=request.user)
    addressdata = UserAddress.objects.filter(user=request.user)
    sum = 0
    for cart in cartdata:
        sum += cart.qty*cart.product.price
    return render(request,"checkout.html",{"carts":cartdata,"total":sum,"addresses":addressdata})

def details(request):
    
    product = Product.objects.get(pk=request.GET['pid'])
    return render(request,"details.html",{'product':product})

def shop(request):
    return render(request,"shop.html")

def loginregister(request):
    return render(request,"login-register.html")


def registeruser(request):
    if request.method=="POST":
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password=data.get("password")

        if User.objects.filter(username=username).exists():
            return render(request,'login-register.html',{'err':"Username exist !!!"})

        user = User(username=username,email=email)
        user.set_password(password)
        user.save()

        return render(request,'login-register.html',{'msg':"Registration success !!!"})
    

def loginuser(request):
    if request.method=="POST":
        data = request.POST
        username = data.get("username")
        password=data.get("password")

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("index")
        
        else:
            return render(request,'login-register.html',{'loginerr':"Invalid Credentials !!!"})


@login_required(login_url="loginregister")
def logoutuser(request):
    logout(request)
    return redirect("index")



def addtocart(request):
    
    if request.user.is_anonymous:
        print(request.user)
        return HttpResponse(request.user)
    else:
    
        pid = request.GET['pid']
        product = Product.objects.get(pk=pid)

        cart = Cart.objects.filter(user=request.user,product=product)
        print(len(cart))
        if len(cart)>0 :
            cart[0].qty = cart[0].qty+1
            cart[0].save()
            return HttpResponse("Product added into cart !!!!")
        else:
            Cart.objects.create(user=request.user,product=product,qty=1)
            return HttpResponse("Product added into cart !!!!")
    

def removecart(request):

    cid = request.GET['cid']
    cart = Cart.objects.get(pk=cid)
    cart.delete()
    return HttpResponse("Cart Item deleted !!!")


def changeqty(request):

    cid = request.GET['cid']
    qty = int(request.GET['qty'])
    cart = Cart.objects.get(pk=cid)
    if qty <=0:
        cart.delete()
    else: 
        cart.qty  =qty
        cart.save()
    return HttpResponse("Cart Item update !!!")


def addadr(request):
    newadr = request.GET['adr']
    UserAddress.objects.create(user=request.user,address=newadr)
    return HttpResponse("address added")

def viewadr(request):
    alladr = UserAddress.objects.filter(user=request.user)
    print(alladr)
    return JsonResponse({"address":list(alladr.values())})


def pay(request):

    amt = int(request.GET['amt'])
   
    client = razorpay.Client(auth=("rzp_test_oox9ZKsz6Uu09W", "1umN06wc9ZHC2blBvuR41bN9"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)  # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    print(payment)
    return JsonResponse(payment)