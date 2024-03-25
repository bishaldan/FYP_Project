# admin.py

from .models import Intent  # Import your Intent model
from .models import Announcement
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


admin.site.register(Announcement)


@admin.register(Intent)
class IntentAdmin(admin.ModelAdmin):
    list_display = ['tag']  # Display the tag field in the admin list view
