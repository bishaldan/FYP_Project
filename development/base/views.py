# from django.shortcuts import render,  redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .models import Student  # Import your Student model
# # Create your views here.


# def home(request):
#     return render(request,  'base/home.html')


# def room(request):
#     return render(request, 'base/room.html')


# def login_page(request):
#     return render(request, 'base/login.html')


# def main_student(request):
#     if request.method == "POST":
#         email = request.POST["email"]  # Updated from "username" to "email"
#         password = request.POST["password"]
#         # Updated from "username" to "email"
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('base/main_student.html')
#         else:
#             messages.error(
#                 request, "Invalid email or password. Please try again.")
#             return redirect('base/login.html')
#     else:
#         return render(request, 'base/main_student.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Student  # Import your Student model


def home(request):
    return render(request, 'base/home.html')


def room(request):
    return render(request, 'base/room.html')


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('base/main_student.html')
        else:
            messages.error(
                request, "Invalid email or password. Please try again.")
            return redirect('login_page')
    else:
        return render(request, 'base/login.html')


def main_student(request):
    return render(request, 'base/main_student.html')


def chatbot_student(request):
    return render(request, 'base/chatbot_student.html')
