from django import forms
from django.core.exceptions import ValidationError
from todo_list.models import Task


class AddTaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Название задачи:',
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 1, 'class': 'edit_task'}),
        max_length=200,
    )

    text = forms.CharField(
        label='Описание задачи:',
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5, 'class': 'edit_task'}),
        max_length=1000,

    )

    class Meta:
        model = Task
        fields = ['title', 'text']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise ValidationError('В названии должно быть минимум 3 символа')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 5:
            raise ValidationError('В описании должно быть минимум 5 символа')
        return text


