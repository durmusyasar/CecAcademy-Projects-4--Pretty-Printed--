from django import forms
from .models import Todo

class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=40, widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter todo e.g. Delete junk files',
                'aria-label' : 'Todo',
                'aria-describedby' : 'add-btn'
            }
        )
    )

class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text' : forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter todo e.g. Delete junk files',
                'aria-label' : 'Todo',
                'aria-describedby' : 'add-btn'
            }
            )
        }