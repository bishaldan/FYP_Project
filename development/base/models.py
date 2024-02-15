from django.db import models
import datetime
# Create your models here.


class Student(models.Model):
    student_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    Year = models.CharField(max_length=10)
    Fee = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Teacher(models.Model):
    Teacher_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Cources(models.Model):
    cources_id = models.CharField(max_length=10)
    cources_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cources_id}'
