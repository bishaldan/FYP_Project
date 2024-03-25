from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Teacher(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Add other fields specific to teachers

    def __str__(self):
        return self.email


class Student(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, default="New_Student")
    last_name = models.CharField(max_length=100, default="")
    fee = models.CharField(default='0.00', max_length=15)
    # Assuming joining year is an integer
    joining_year = models.CharField(max_length=100, default="")
    field_of_study = models.CharField(max_length=100, default="")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Announcement(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
# models.py


# models.py
class Intent(models.Model):
    tag = models.CharField(max_length=100)
    patterns = models.JSONField()
    responses = models.JSONField()
