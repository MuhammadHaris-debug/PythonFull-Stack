from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello,world! This is my first Django app.")

def about(request):
    return HttpResponse("this is about page of my first Django app.")

def contact(request):
    return HttpResponse("contact as here for my first Django app.")


# def student(Request):
#     return render(Request, 'student.html')
