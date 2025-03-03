from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    return render(request,"index.html",{"title":"Index"})

def home(request):
    #return HttpResponse("home")
    return render(request,"home.html",{"title":"Home"})

def about(request):
        # return HttpResponse("about")
    return render(request,"about.html",{"title":"About"})
