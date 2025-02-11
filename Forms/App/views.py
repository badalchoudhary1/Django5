from django.shortcuts import render, redirect
from .forms import EmployeeModelForm
from .models import Employee

# View for handling form submission


def employee_create(request):
    if request.method == "POST":
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect after saving
    else:
        form = EmployeeModelForm()
    return render(request, 'employee_form.html', {'form': form})

# View to display employees


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
