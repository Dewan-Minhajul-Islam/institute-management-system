from django.shortcuts import render
from students.models import StudentModel

# Create your views here.
def student_view(request):
    
    std_data = StudentModel.objects.all()
    
    context = {
        'std_data' : std_data
    }
    
    return render(request, 'student-list.html', context)