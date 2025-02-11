from django.urls import path
from .views import employee_create, employee_list

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('create/', employee_create, name='employee_create'),
]
