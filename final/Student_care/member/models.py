from django.db import models

# Create your models here.


class user_members(models.Model):
    Student_email = models.CharField(max_length=50)
    Student_name = models.CharField(max_length=50)
    student_password = models.CharField(max_length=100)
    teacher_email = models.CharField(max_length=50)
    teacher_password = models.CharField(max_length=100)
    Year = models.CharField(max_length=10)
    Fee = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.Student_name_name}{self.teacher_email}'
