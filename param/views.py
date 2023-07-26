from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
def home(request):
    all=Employee.objects.all()
    all1=Employee.objects.all().count()
    context={
        "emp":all,
        "emp10":all1
    }
    return render(request,"home.html",context)

def add(request):
    if request.method=="POST":
        sample=EmployeeForm(request.POST)
        if sample.is_valid():
            sample.save()
            return redirect("home")
    sample=EmployeeForm()
    return render(request,"add.html",context={"data":sample})
    
def edit(request,id):
    instance=Employee.objects.get(id=id)
    if request.method=="POST":
        sample2=EmployeeForm(request.POST,instance=instance)
        if sample2.is_valid():
            sample2.save()
        return redirect("home")
    sample2=EmployeeForm(instance=instance)
    return render(request,"edit.html",context={"denim":sample2})

def delhi(request,id):
    emp4=Employee.objects.get(id=id).delete()
    return redirect("home")

def delall(request):
    emp4=Employee.objects.all().delete()
    return redirect("home")
