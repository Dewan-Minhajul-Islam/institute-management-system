from django.shortcuts import render, redirect
from django.contrib import messages
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
    if request.method == 'POST':
        form_data = StudentForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Student Register Successfully')
            return redirect('student_view')
    
    
    context = {
        'form_title' : 'Add Student Information',
        'form_btn' : 'Add Student',
        'page_title' : 'Student Register',
        'form_data' : form_data
    }
    
    return render(request, 'layout/base-form.html', context)