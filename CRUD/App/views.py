from django.shortcuts import render
from .models import Employee
from django.shortcuts import redirect, get_object_or_404


def create_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Employee.objects.create(name=name, email=email, password=password)
        # Redirect to the list of employees
        return redirect("get_all_employee")
    return render(request, 'add_employee.html')  # Show form for GET request


def get_all_employee(request):
    employees = Employee.objects.all()  # Get all employees
    return render(request, 'get_all_employee.html', {"Employees": employees})


def get_employee(request, id):
    y = get_object_or_404(Employee, id=id)
    return render(request, 'get_employee.html', {'employee': y})


def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.password = request.POST.get('password')
        employee.save()
        return redirect('get_all_employee')
    return render(request, 'edit_employee.html', {'employee': employee})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('get_all_employee')
