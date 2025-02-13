from django.db import models

# Create your models here.


class Student (models.Model):
    name = models.CharField(max_length=100)
    code= models.CharField(max_length=12)
    gender = models.BooleanField()
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Courses (models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField()
    def __str__(self):
        return f"{self.name} - {self.start_date} - {self.end_date} - {self.active}"