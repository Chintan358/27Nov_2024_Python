from django.shortcuts import render,redirect
from myapp.models import *
from django.core.paginator import Paginator
# Create your views here.
from django.db.models import Sum
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
def index(request):

    allStudents = Student.objects.all()
    paginator = Paginator(allStudents, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"students":page_obj})

def result(request,id):
    
    studentid = StudentID.objects.get(student_id=id)
    student = Student.objects.get(studentid=studentid)
    studentmarks = Marks.objects.filter(student=student)

    # sum = 0
    # for i in studentmarks:
    #     sum+=i.marks
    total = studentmarks.aggregate(total=Sum('marks'))

    
    rank =  Student.objects.annotate(totalmarks = Sum("marks__marks")).order_by("-totalmarks")
    
    count  = 0
    for i in rank:
        count+=1
        if i.studentid.student_id == id:
            break


    return render(request,"result.html",{"marks":studentmarks,"sum":total,"rank":count})


def sendmail(request,id):
    studentid = StudentID.objects.get(student_id=id)
    student = Student.objects.get(studentid=studentid)
    studentmarks = Marks.objects.filter(student=student)

    # sum = 0
    # for i in studentmarks:
    #     sum+=i.marks
    total = studentmarks.aggregate(total=Sum('marks'))

    
    rank =  Student.objects.annotate(totalmarks = Sum("marks__marks")).order_by("-totalmarks")
    
    count  = 0
    for i in rank:
        count+=1
        if i.studentid.student_id == id:
            break


    html_message = render_to_string('result.html',{"marks":studentmarks,"sum":total,"rank":count})
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [studentmarks[0].student.email]
    send_mail( "Report Card", plain_message, email_from, recipient_list ,html_message=html_message)
    
    return redirect("index")
 