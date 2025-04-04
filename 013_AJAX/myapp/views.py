from django.shortcuts import render,HttpResponse
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def test(request):
    value = request.GET['value']
    data = ""
    if value == 'sports':
        data+="<ul><li>Cap</li><li>Bat</li><li>Ball</li></ul>"
    elif value == 'cloths':
        data+="<ul><li>Tshirt</li><li>Shirt</li><li>Cap</li></ul>"
    return HttpResponse(data)
    

def country(request):
    allconutris = Country.objects.all()
    return JsonResponse({"data":list(allconutris.values())})



def state(request):
    cid = request.GET['cid']
    allstates = State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(allstates.values())})

def city(request):
    sid = request.GET['sid']
    allcities = City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(allcities.values())})