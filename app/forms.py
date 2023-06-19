from django import forms
from .models import Courses, Lesson, Comment


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['name', 'desc', 'price']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'course', 'video', 'description']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Comment here...',
        'rows':4,
        'cols':50
        }))
    class Meta:
        model = Comment
        fields = ['content']

