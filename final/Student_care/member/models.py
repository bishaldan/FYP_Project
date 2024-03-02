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
    fee = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Announcement(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
