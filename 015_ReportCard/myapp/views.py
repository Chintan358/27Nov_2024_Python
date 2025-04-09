from django.shortcuts import render
from myapp.models import *
from django.core.paginator import Paginator
# Create your views here.
from django.db.models import Sum
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
    
    return render(request,"result.html",{"marks":studentmarks,"sum":total})