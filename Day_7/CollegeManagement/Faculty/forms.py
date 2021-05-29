from django.forms import ModelForm
from .models import *

class Facultyform(ModelForm):
    class Meta:
        model = Faculty
        # fields = ['Name','Branch']
        fields = '__all__' # all fields 
