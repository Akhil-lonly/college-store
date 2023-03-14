from django.contrib import admin
from .models import Course, Department, Student_Form


# Register your models here
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course']
admin.site.register(Course,CourseAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department']
admin.site.register(Department,DepartmentAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['NAME','DOB','AGE','GENDER','PHONE_NUMBER',
                    'MAIL_ID','ADDRESS','DEPARTMENT','COURSE','PURPOSE']
admin.site.register(Student_Form,StudentAdmin)