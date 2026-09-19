from django.shortcuts import render,redirect
from .models import Student

def create_students(request):
    if request.method =='POST':
        name=request.POST['name']
        age=request.POST['age']
        course=request.POST['course']

        Student.objects.create(name=name,age=age,course=course)

        return redirect('display_students')

    return render(request,'student.html')


def display_students(request):
    student=Student.objects.all()
    return render(request, 'display.html',{'i':student})
