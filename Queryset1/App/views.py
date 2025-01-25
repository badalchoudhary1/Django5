from django.shortcuts import render
from .models import Student
# Create your views here.


def home(request):
    # student_data = Student.objects.get(id=1)  # this will give you data of student with id 1
    # student_data = Student.objects.first() # This will give the first student data
    # student_data = Student.objects.last()    # This will give the last student data

    # This will give the first student data in ascending order of name
    # student_data = Student.objects.order_by('name').first()

    # student_data = Student.objects.order_by('name').last() # This will give the last student data in ascending order of name
    # student_data = Student.objects.latest('pass_date')  # This will give the latest student data based on pass_date

    # student_data = Student.objects.latest('pass_date','id') # This will give the latest student data based on pass_date and if pass_date is same then it will give the latest student data based on id
    # student_data = Student.objects.earliest('pass_date')

    # student_data = Student.objects.create(
    #     name="Rohan", roll=104, city="Rampur", marks=90, pass_date='2021-06-12')

    # student_data, created = Student.objects.get_or_create(
    #     name="tinku", roll=1022, city="Rampur", marks=90, pass_date='2021-06-12')
    # student_data = Student.objects.filter(id=1).update(marks=100)
    student_data = Student.objects.filter(id=1).delete()

    # student_data, created = Student.objects.update_or_create(id=1, name="badal", defaults={
    #                                                          'name': 'Rohan', 'roll': 212, 'city': 'Rampur', 'marks': 90, 'pass_date': '2021-06-12'}) # This will update the student data with id 1 if it exists otherwise it will create a new student data with id 1
    return render(request, 'home.html', {'student': student_data})
