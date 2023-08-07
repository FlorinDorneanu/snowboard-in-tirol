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
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Write your opinion ', 'required': False}),
        }

