from .models import Announcement
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    field_of_study_choices = [
        ('BSC (HONS) COMPUTING', 'BSC (HONS) COMPUTING'),
        ('BSC (HONS) COMPUTER NETWORKING & IT SECURITY',
         'BSC (HONS) COMPUTER NETWORKING & IT SECURITY'),
        ('BSC (HONS) COMPUTING WITH ARTIFICIAL INTELLIGENCE',
         'BSC (HONS) COMPUTING WITH ARTIFICIAL INTELLIGENCE'),
        ('BSC (HONS) MULTIMEDIA TECHNOLOGIES',
         'BSC (HONS) MULTIMEDIA TECHNOLOGIES'),
    ]

    field_of_study = forms.ChoiceField(
        choices=field_of_study_choices, widget=forms.Select)

    class Meta:
        model = Student
        fields = ['email', 'password', 'first_name',
                  'last_name', 'fee', 'joining_year', 'field_of_study']


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['text']


class FeeStatusCheckForm(forms.Form):
    email = forms.EmailField(label='Enter your email')
    password = forms.CharField(
        label='Enter your password', widget=forms.PasswordInput)
