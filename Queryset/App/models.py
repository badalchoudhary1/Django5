from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    pass_date = models.DateField()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=100)
    salary = models.IntegerField()
    join_date = models.DateField()
