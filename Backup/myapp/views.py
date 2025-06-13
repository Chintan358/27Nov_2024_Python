from django.shortcuts import render,HttpResponse
import razorpay
from django.http import JsonResponse


# Create your views here.
def index(request):
    """
    Render the home page of the application.
    """
    return render(request, 'index.html')  # Ensure you have an index.html in your templates/myapp directory


def payment(request):
    
    amount = int(request.GET.get('amount'))  
    client = razorpay.Client(auth=("rzp_test_oox9ZKsz6Uu09W", "1umN06wc9ZHC2blBvuR41bN9"))

    data = { "amount": amount*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    
    return JsonResponse(payment)  # Ensure you handle the response properly, e.g., render a template or return JSON