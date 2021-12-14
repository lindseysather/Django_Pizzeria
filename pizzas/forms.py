from django import forms

from .models import Image, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        labels = {'name':''}
