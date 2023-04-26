
from django import forms

from task.models import Task


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'folder', 'color', 'completionDate')

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Title', "required": True}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description', 'cols': '30', 'rows': '10'}),
            'completionDate': forms.TextInput(
                attrs={'type': 'datetime-local', 'step': '60', "required": True})
        }




