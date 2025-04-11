from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
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