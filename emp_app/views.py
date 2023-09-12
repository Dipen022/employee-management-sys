from django.shortcuts import render,HttpResponse
from .models import Employees, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html' )

def all_emp(request):
    emps = Employees.objects.all()
    context = {

        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context )

def add_emp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        Role = int(request.POST['Role'])
        new_emp = Employees(firstname= firstname,lastname= lastname, salary= salary, bonus= bonus, phone= phone, dept_id= dept, role_id= Role , hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added succesfully')
        
    elif request.method == 'GET':
        

        return render(request, 'add_emp.html' )
    else:
        return HttpResponse("An Exception Occured! Employee has Not Been Added")
        
    


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employees.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Deleted Successfully")
        except Employees.DoesNotExist:
            return HttpResponse("Please Enter a valid EMP ID")
        except Exception as e:
            return HttpResponse("An error occurred while deleting the employee")
            
    emps = Employees.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST': 
        name = request.POST['name']
        dept = request.POST['dept']
        Role = request.POST['Role']
        emps = Employees.objects.all()
        if name:
            emps = emps.filter(Q(firstname__icontains = name) | Q(lastname__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if Role:
            emps = emps.filter(Role__name__icontains = Role)

        context = {
            'emps': emps
        }
        return render(request,'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception occured')
    