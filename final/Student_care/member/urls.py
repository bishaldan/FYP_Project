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

]
