from django.forms import ModelForm
from .models import Student2
class StudentForm(ModelForm):
    class Meta:
        model=Student2
        fields="__all__"