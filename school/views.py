from django.shortcuts import render,redirect
from .forms import *
from .models import *
def home(req):
    form=StudentForm(req.POST or None)
    data={
        "student":Student2.objects.all(),
        "form":form
    }
    if req.method == "POST":
       if form.is_valid():
           form.save()
           return redirect(home)
    return render(req,"index.html",data)
def deleteF(req,id):
    student = Student2.objects.get(pk=id)
    student.delete()
    return redirect(home)

def editStudent(req,id):
    student=Student2.objects.get(pk=id)
    form = StudentForm(req.POST or None,instance=student)
    if req.method == "POST":
       if form.is_valid():
           form.save()
           return redirect(home)
    return render(req,"edit.html",{"form":form})