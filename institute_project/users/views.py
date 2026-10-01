from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login_view(request):
    
    form_data = AuthenticationForm()
    
    
    context = {
        'form_data' : form_data
    }
    
    return render(request, 'login.html', context)