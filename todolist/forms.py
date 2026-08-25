from django import forms
from .models import ToDoList

class CreateTask(forms.Form):
    Creattast = forms.CharField(label="Enter Task", max_length=100)
