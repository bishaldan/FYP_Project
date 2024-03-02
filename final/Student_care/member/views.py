from .forms import AnnouncementForm
from datetime import datetime
from django.contrib import messages
from django.contrib import messages  # Import messages module
from .forms import StudentForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Teacher, Student
from .models import Announcement
from .forms import AnnouncementForm  # You need to define this form

# Create your views here.


def index(request):
    return render(request,  'member/index.html')


# views.py


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user is a student
        student = Student.objects.filter(
            email=email, password=password).first()
        if student:
            # Redirect to student dashboard
            return redirect('student_dashboard')

        # Check if the user is a teacher
        teacher = Teacher.objects.filter(
            email=email, password=password).first()
        if teacher:
            # Redirect to teacher dashboard
            return redirect('teacher_dashboard')

        # Authentication failed
        return render(request, 'member/login.html', {'error': 'Invalid credentials'})

    return render(request, 'member/login.html')


def student_dashboard(request):
    return render(request, 'member/student_dashboard.html')


def teacher_dashboard(request):
    return render(request, 'member/teacher_dashboard.html')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            # Get the name of the student that was added
            student_name = f'{student.first_name} {student.last_name}'
            # Add success message with the student's name
            messages.success(request, f'{student_name} added successfully')
            return redirect('add_student')
    else:
        form = StudentForm()
    return render(request, 'member/add_student.html', {'form': form})


def announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.posted_date = datetime.now()
            announcement.save()
            messages.success(
                request, f'Announcement posted successfully on {announcement.posted_date.strftime("%Y-%m-%d %H:%M:%S")}')
            return redirect('view_announcement')
    else:
        form = AnnouncementForm()
    return render(request, 'member/announcement.html', {'form': form})


def get_announcement(request):
    # # Logic to fetch announcements from the database
    # # Example query, adjust as per your model
    announcements = Announcement.objects.all()

    return render(request, 'member/get_announcement.html', {'announcements': announcements})
