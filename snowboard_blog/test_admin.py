from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from .admin import PostAdmin, CommentAdmin
from django.urls import reverse
from django.utils import timezone


class AdminTestCase(TestCase):
    def setUp(self):
        # Create a superuser for testing
        self.user = User.objects.create_superuser(
            username='admin', password='password', email='admin@example.com'
        )
        self.client.login(username='admin', password='password')

    def test_post_admin(self):
        # Create a post instance
        post = Post.objects.create(
            title='Test Post', content='This is a test post content.',
            slug='test-post', status=1, created_on=timezone.now()
        )

        # Check if the post is registered in the admin and accessible
        response = self.client.get(
            reverse('admin:snowboard_blog_post_change', args=[post.id]))
        self.assertEqual(response.status_code, 200)

        # Check if the PostAdmin class is used for Post model
        self.assertIsInstance(
            response.context['adminform'].form, PostAdmin.form)

    def test_comment_admin(self):
        # Create a comment instance
        comment = Comment.objects.create(
            post=Post.objects.create(
                title='Test Post', content='This is a test post content.',
                slug='test-post', status=1, created_on=timezone.now()
            ),
            name='Test User', email='test@example.com', body='This is a test comment.',
            created_on=timezone.now(), approved=False
        )

        # Check if the comment is registered in the admin and accessible
        response = self.client.get(
            reverse('admin:snowboard_blog_comment_change', args=[comment.id]))
        self.assertEqual(response.status_code, 200)

        # Check if the CommentAdmin class is used for Comment model
        self.assertIsInstance(
            response.context['adminform'].form, CommentAdmin.form)

    def test_approve_comments_action(self):
        # Create a comment instance
        comment = Comment.objects.create(
            post=Post.objects.create(
                title='Test Post', content='This is a test post content.',
                slug='test-post', status=1, created_on=timezone.now()
            ),
            name='Test User', email='test@example.com', body='This is a test comment.',
            created_on=timezone.now(), approved=False
        )

        # Approve the comment using the custom action
        self.client.post(reverse('admin:snowboard_blog_comment_changelist'), data={
            'action': 'approve_comments', '_selected_action': [comment.id]
        })

        # Check if the comment is approved
        comment.refresh_from_db()
        self.assertTrue(comment.approved)
