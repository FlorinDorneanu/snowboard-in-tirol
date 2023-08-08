from django.test import TestCase
from .forms import CommentForm
from .models import Comment


class CommentFormTestCase(TestCase):
    def test_comment_form_valid_data(self):
        # Create a valid form instance
        form_data = {'body': 'This is a test comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_data(self):
        # Create an invalid form instance
        form_data = {}  # Empty data
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_comment_form_save(self):
        # Create a comment instance using the form
        form_data = {'body': 'This is a test comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

        comment = form.save(commit=False)
        self.assertEqual(comment.body, form_data['body'])
        self.assertIsInstance(comment, Comment)
