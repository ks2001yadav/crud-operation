from django.shortcuts import render,HttpResponse,redirect
from home.models import Employee
from datetime import datetime
from typing import ContextManager
from django.contrib import messages

# Create your views here.
def index(request):

    return render(request,"index.html")

def login(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        field=request.POST.get('field')
        salary=request.POST.get('salary')
        employee=Employee(name=name,phone=phone,address=address,field=field,salary=salary,date=datetime.today())
        employee.save()
        messages.success(request, 'Profile details updated.')
    return render(request,"login.html")

def logout(request):
    return render(request,"index.html")

def details(request):

    data = Employee.objects.all()
    #data = Employee.objects.filter(name__startswith='k')
    # data = Employee.objects.filter(address='kaithal')
    stu = {
    "s": data
    }
   
    return render(request,"details.html",stu)

def edit(request,id):
    employee = Employee.objects.filter(id=id)[0] 
    Employee.objects.filter(id=id).delete()
    return render(request, 'edit.html', {'employee': employee})  

def delete(request,id):
    Employee.objects.filter(id=id).delete()
    return render(request, 'details.html') 

def update(request,id):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        field=request.POST.get('field')
        salary=request.POST.get('salary')
        employee=Employee(name=name,phone=phone,address=address,field=field,salary=salary,date=datetime.today())
        employee.save()
        
    return redirect('/details')   