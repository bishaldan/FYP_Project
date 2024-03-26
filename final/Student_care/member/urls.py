from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_page, name='login_page'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    # URL pattern for adding a student
    path('add_student/', views.add_student, name='add_student'),
    # URL pattern for viewing announcements
    path('announcement/', views.announcement, name='announcement'),
    path('get_announcement/', views.get_announcement, name='get_announcement'),


    path('announcement_student/', views.announcement_student,
         name='announcement_student'),
    # URL pattern for fee Status
    path('fee_status/', views.fee_status, name='fee_status'),
    path('payment/', views.payment_page, name='payment_page'),
    # path('chatbot/', views.chat_with_bot, name='chatbot')

    path('edit_studnt/', views.edit_student, name='edit_student'),

    path('get', views.chatbot_response, name='get_bot_response'),
    path('chatbot/', views.home, name='home'),




]
