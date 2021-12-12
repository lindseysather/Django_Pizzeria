from django import forms

from .models import Image, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        labels = {'name':''}

class ImageForm(forms.ModelForm):
    '''Form for the image model'''
    class Meta:
        model = Image
        fields = ('title', 'image')