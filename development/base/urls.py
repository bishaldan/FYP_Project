from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('login/', views.login_page, name='login_page'),
    path('main_student/', views.main_student, name='main_student'),
    path('chatbot/', views.chatbot_student, name='chatbot_student'),
]
