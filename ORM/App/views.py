from django.shortcuts import render
from .models import Student
# Create your views here.


def all_data(request):
    students = Student.objects.all()
    print(students)
    return render(request, 'all.html', {'student': students})


def single_data(request):
    student = Student.objects.get(id=1)
    print(student)
    return render(request, 'single.html', {'stu': student})
