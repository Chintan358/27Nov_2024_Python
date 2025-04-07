from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=50)

class StudentID(models.Model):
    student_id = models.CharField(max_length=20)

class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    studentid = models.ForeignKey(StudentID,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

class Subject(models.Model):
    subject_name = models.CharField(max_length=20)

class Marks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.IntegerField()