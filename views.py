# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from Employee.forms import EmployeeForm  
from employee.models import Employee  
# Create your views here.  
def CreatEmpData(request):  
    if request.method == "POST":  
    	form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
        return render(request,'index.html',{'form':form})  
def ShowDetails(request):  
    employee = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def EditDetails(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def UpdateDetails(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def delete(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
