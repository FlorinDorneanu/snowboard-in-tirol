'''
forms.py

This module contains Django forms used in the application.

- CommentForm: A form used for submitting comments, including support for nested comments.
'''

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    parent_id = forms.IntegerField(
        widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ('body', 'parent_id')
