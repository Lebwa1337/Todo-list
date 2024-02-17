from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'time'}))

    class Meta:
        model = Task
        fields = ["content", "deadline", "tag",]
