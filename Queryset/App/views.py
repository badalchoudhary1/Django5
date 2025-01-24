from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.


def home(request):
    # all_data = Student.objects.all() # It will give you all the data
    # It will give you the data of marks 23
    all_data = Student.objects.filter(marks=23)
    # all_data = Student.objects.filter(name='ror') # It will give you the data of ror
    # all_data = Student.objects.exclude(name='ror') # It will exclude the data of ror
    # all_data = Student.objects.order_by('marks') # It will give you the data in ascending order
    # all_data = Student.objects.order_by('-marks') # It will give you the data in descending order
    # all_data = Student.objects.order_by('?')  # Random data give by ? method
    # all_data = Student.objects.order_by('name')[0:2] # It will give you the data of 0 to 2
    # all_data = Student.objects.order_by('name').reverse() # It will give you the data in reverse order
    # all_data = Student.objects.values('name', 'city') # It will give you the data in the form of dictionary in a list
    # all_data = Student.objects.values() # It will give you the data in the form of dictionary in a list
    # It will give you the data in the form of tuple in a list
    # all_data = Student.objects.values_list('id', 'name', named=True) # It will give you the data in the form of tuple in a list and the named=True is used to give the name of the tuple without named=True it will give you the data in the form of tuple without name

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # # It will give you the data of both the tables in the form of tuple in a list
    # all_data = qs1.union(qs2)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # # It will give you the data of both the tables in the form of tuple in a list and the all=True is used to give you the data of both the tables
    # all_data = qs1.union(qs2, all=True)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # # It will give you the data of both the tables in the form of tuple in a list and the intersection is used to give you the common data of both the tables
    # all_data = qs1.intersection(qs2)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # # It will give you the data of both the tables in the form of tuple in a list and the difference is used to give you the data of first table which is not in the second table
    # all_data = qs1.difference(qs2)

    # all_data = Student.objects.filter(name='badal') & Student.objects.filter(
    #     city='shamli') # It will give you the data of both the conditions which is true

    # It will give you the data of both the conditions
    # all_data = Student.objects.filter(name='badal', city='karnal')

    # all_data = Student.objects.filter(name='badal') | Student.objects.filter(
    #     city='mkmk')  # it will give you the data of any one condition which is true

    print(all_data)
    # print()
    # print('SQL Query', all_data.query) # To see the SQL Query and they give you the data in the form of SQL Query after refresh the page
    return render(request, 'home.html', {'all_data': all_data})
