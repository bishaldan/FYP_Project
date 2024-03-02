# admin.py

from django.contrib import admin
from .models import Teacher, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view
    list_display = ('email',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Customize the fields displayed in the admin list view
    list_display = ('email',)
