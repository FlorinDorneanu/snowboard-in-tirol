# * Import the necessary module from Django *
from .models import Comment
from django import forms


# * Define a form for submitting comments *
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

# * Define a form for editing comments *
class EditForm(forms.ModelForm):
    """
    Form to edit a comment from the user.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            "body": "Make your changes below and click save",
        }
