'''
forms.py

This module contains Django forms used in the application.

- CommentForm: A form used for submitting comments.
'''

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
