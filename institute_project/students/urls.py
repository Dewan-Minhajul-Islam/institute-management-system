from django.urls import path
from students.views import *


urlpatterns = [
    path('student-list/', student_view, name='student_view'),
    path('add-student/', student_form, name='student_form'),
]
