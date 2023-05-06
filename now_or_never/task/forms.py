
from django import forms

from task.models import Task, Folder


class FolderCreateForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('name',)


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'folder', 'color', 'completionDate', 'isDone')

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Title', "required": True}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description', 'cols': '30', 'rows': '20'}),
            'completionDate': forms.TextInput(
                attrs={'type': 'datetime-local', 'step': '60', "required": True}),
            'isDone': forms.CheckboxInput(
                attrs={'id': 'update-isDone-checkbox'}
            )

        }
