from django.shortcuts import render,redirect
from .forms import *
from .models import *
def home(req):
    form=StudentForm(req.POST or None)
    formT=TeacherForm(req.POST or None)
    data={
        "student":Student2.objects.all(),
        "form":form,
        "teacher":Teacher.objects.all(),
        "formT":formT,
    }
    if req.method == "POST":
       if formT.is_valid():
           formT.save()
           return redirect(home)
    if req.method == "POST":
       if form.is_valid():
           form.save()
           return redirect(home)

    return render(req,"index.html",data)
def homeTeacher(req):
    formT=TeacherForm(req.POST or None)
    data={
        "teacher":Teacher.objects.all(),
        "formT":formT,
    }
    if req.method == "POST":
       if formT.is_valid():
           formT.save()
           return redirect(homeTeacher)
    

    return render(req,"indexTeacher.html",data)
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
def search(req):
    if req.method=="GET":
        search_query=req.GET.get("search")
        form=StudentForm()
        data={
            "student":Student2.objects.filter(name__icontains=search_query),
            "form":form
        }
        return render(req,"index.html",data)
def  filter(req):
    if req.method =="GET":
        search=req.GET.get("city")
        form = Student2
        data={
            "student":Student2.objects.filter(city=search),
            "form":form
        }
        return render(req,"index.html",data)
