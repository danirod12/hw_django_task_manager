from django import forms
from .models import Task, Category, Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description (optional)',
                'rows': 3
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        existing = Category.objects.filter(name=name).exclude(pk=self.instance.pk)
        if existing.exists():
            raise forms.ValidationError('Category with this name already exists')
        return name


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'is_done', 'category', 'executor', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                'rows': 3
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'is_done': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'executor': forms.Select(attrs={
                'class': 'form-control'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Enter your comment',
                'rows': 3
            }),
        }
        labels = {
            'text': 'Comment'
        }
