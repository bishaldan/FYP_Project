from .models import Announcement
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password', 'first_name', 'last_name', 'fee']


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['text']
