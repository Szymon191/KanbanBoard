from django import forms
from .models import Task


class addForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'body', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'body': forms.Textarea(attrs={'class': 'input'}),
            'status': forms.Select(attrs={'class': 'input'})
        }
