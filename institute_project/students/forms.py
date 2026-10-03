from django import forms
from students.models import StudentModel
from users.models import UserModel


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = ['user']

