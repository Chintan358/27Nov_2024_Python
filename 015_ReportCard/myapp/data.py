from faker import Faker
fake = Faker()
import random
from myapp.models import *

def generate(n=50):
    for i in range(n):
        name = fake.name()
        email = fake.email()
        age = random.randint(20,30)
        student_id = f"STD_{random.randint(100,999)}"
        stid =  StudentID.objects.create(student_id=student_id)
        allDept = Department.objects.all()
        dept  = allDept[random.randint(0,len(allDept)-1)]

        Student.objects.create(department=dept,studentid=stid,name=name,age=age,email=email)

def addmarks():
    allStudents  =Student.objects.all()
    for student in allStudents:
        allsubject = Subject.objects.all()
        for subject in allsubject:
            marks = random.randint(1,100)

            Marks.objects.create(student=student,subject=subject,marks=marks)