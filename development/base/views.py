from django.shortcuts import render,  redirect

# Create your views here.


def home(request):
    return render(request,  'base/home.html')


def room(request):
    return render(request, 'base/room.html')


def main_student(request):
    return render(request, 'base/main_student.html')


def chatbot_student(request):
    return render(request, 'base/chatbot_student.html')
