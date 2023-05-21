from django.shortcuts import render, HttpResponseRedirect
from .models import Student
from .forms import StudentAddForm,StudentUpdateForm


# Create your views here.


def index(req):
    students = Student.objects.all()
    return render(req,"student/index.html",{"students":students})

def add(req):
    if req.method == 'POST':
        form = StudentAddForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/student")
    else:
        form = StudentAddForm()

    return render(req, 'student/add-student.html', {'form': form})


def update(req,id):
    student=Student.objects.get(id=id)
    if req.method == 'POST':
        form = StudentUpdateForm(req.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/student")
    else:
        form = StudentUpdateForm(instance=student)

    return render(req, 'student/update-student.html', {'form': form})

def delete(req,id):
    return HttpResponseRedirect("/student")
