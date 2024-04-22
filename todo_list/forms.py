from django import forms
from todo_list.models import Task


class AddTaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Название задачи:',
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 1, 'class': 'edit_task'}),
    )

    text = forms.CharField(
        label='Описание задачи:',
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5, 'class': 'edit_task'}),
    )

    class Meta:
        model = Task
        fields = ['title', 'text']


