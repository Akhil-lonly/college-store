from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import Department, Student_Form


def home(request):
    return render(request, "index 1.html")


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Successfully")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "The password and confirmation password do not match.")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('home')


def studentform(request):
    dept = Department.objects.all()
    if request.method == 'POST':
        try:
            name = request.POST['name']
            age = request.POST['age']
            dob = request.POST['dob']
            phonenumber = request.POST['phone']
            gender = request.POST['gender']
            address = request.POST['address']
            mailid = request.POST['email']
            department = request.POST['department']
            course = request.POST['course']
            material = request.POST['material']
            purpose = request.POST['purpose']
            student = Student_Form.objects.create(NAME=name, DOB=dob, AGE=age, PHONE_NUMBER=phonenumber,
                                                  GENDER=gender, ADDRESS=address, MAIL_ID=mailid,
                                                  DEPARTMENT=dept.get(pk=department),
                                                  COURSE=course, MATERIAL=material, PURPOSE=purpose)
            student.save()
            messages.success(request, "Succesfully created.")
            return redirect('studentform')

        except ValidationError or ValueError :
            messages.success(request, "Please fill the form properly")
            return redirect('studentform')

    context = {
        'dept': dept,
    }
    return render(request, "studentform.html", context)


def course_finder(request):
    dept = request.GET['dept']
    department = Department.objects.filter(id=dept).all()[0]
    print(request.GET['dept'])
    j = render_to_string('courses.html', {'dept': department.courses.all()})
    return JsonResponse({'depart': j})
