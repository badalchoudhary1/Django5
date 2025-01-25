from django.shortcuts import render
from .models import Student
# Create your views here.


def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(name__exact='sonu')
    # student_data = Student.objects.filter(name__iexact='Sonu')
    # student_data = Student.objects.filter(name__contains='n')
    # student_data = Student.objects.filter(name__icontains='n')
    # student_data = Student.objects.filter(marks__gt=130)
    # student_data = Student.objects.filter(marks__gte=130)
    # student_data = Student.objects.filter(marks__lt=130)
    # student_data = Student.objects.filter(name__startswith='s')
    # student_data = Student.objects.filter(name__istartswith='s')
    # student_data = Student.objects.filter(name__endswith='u')
    # student_data = Student.objects.filter(name__iendswith='U')
    # student_data = Student.objects.filter(
    #     pass_date__range=('2025-01-01', '2025-12-31'))

    student_data = Student.objects.filter(
        pass_date__year='2025')
    return render(request, 'home.html', {'students': student_data})
