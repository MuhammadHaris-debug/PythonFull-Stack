
from django.views.generic import *
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

from django.views.generic import DetailView

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'


# from django.views.generic import CreateView

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'age']
    template_name = 'student_form.html'
    success_url = '/students/'

from django.views.generic import UpdateView

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'age']
    template_name = 'student_update.html'
    success_url = '/students/'


from django.views.generic import DeleteView

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = '/students/'

    