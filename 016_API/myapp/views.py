from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
# Create your views here.
import razorpay
def index(request):
    return render(request,"index.html")

def sendmail(request):
    context = {}
    address = "chintan.tops@gmail.com"
    subject = "Test"
    message = "Testing..."

    if address and subject and message:
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
            context['result'] = 'Email sent successfully'
        except Exception as e:
            context['result'] = f'Error sending email: {e}'
    else:
        context['result'] = 'All fields are required'
    
    return HttpResponse(context['result'])
    pass


def pay(request):

    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_pv6FbtEGoD0n4P", "iladq0iIJ4h3mt2LyxAalTuK"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)  # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
   
    return JsonResponse(payment)

def payment(request):
    return render(request,"payment.html")