from django.shortcuts import render
from students.models import StudentModel
from students.forms import *


# Create your views here.
def student_view(request):
    
    std_data = StudentModel.objects.all()
    
    context = {
        'std_data' : std_data
    }
    
    return render(request, 'student-list.html', context)


def student_form(request):
    
    form_data = StudentForm()
    
    context = {
        'form_title' : 'Add Student Information',
        'form_btn' : 'Add Student',
        'page_title' : 'Student Register',
        'form_data' : form_data
    }
    
    return render(request, 'layout/base-form.html', context)