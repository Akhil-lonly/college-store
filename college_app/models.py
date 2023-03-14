from django.db import models
from django.urls import reverse

class Course(models.Model):
    course = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.course

class Department(models.Model):
    department = models.CharField(max_length=255,unique=True)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.department

GENDER_CHOICES = [
    ('Female','Female'),
    ('Male','Male'),
    ('Transgender','Transgender'),

]
PURPOSE_CHOICES = [
    ('Enquiry','Enquiry'),
    ('Place Order','Place Order'),
    ('Return','Return'),

]
class Student_Form(models.Model):
    NAME = models.CharField(max_length=255)
    DOB = models.DateField()
    AGE = models.IntegerField()
    GENDER = models.CharField(max_length=255,choices=GENDER_CHOICES)
    PHONE_NUMBER = models.IntegerField()
    MAIL_ID = models.CharField(max_length=255)
    ADDRESS = models.TextField(max_length=1000)
    DEPARTMENT = models.ForeignKey(Department,on_delete=models.CASCADE)
    COURSE = models.CharField(max_length=255,default="B.Sc",null=True)
    PURPOSE = models.CharField(max_length=255,choices=PURPOSE_CHOICES)
    MATERIAL = models.CharField(max_length=255)