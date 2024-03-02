from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,  'member/index.html')


def login_page(request):
    return render(request,  'member/login.html')
