from django.forms import ModelForm
from .models import *
class StudentForm(ModelForm):
    class Meta:
        model=Student2
        fields="__all__"
        
class TeacherForm(ModelForm):
    class Meta:
        model=Teacher
        fields="__all__"
        