from django.shortcuts import render,redirect
from .forms import studentForm

def add_student(request):

    if request.method =='POST':
        form=studentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_student')

    else:
        form=studentForm()

    return render(request,'student.html',{'form':form})
    


# Create your views here.
