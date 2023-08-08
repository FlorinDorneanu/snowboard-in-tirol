from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class ModelsTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

    def test_post_model(self):
        # Create a post instance
        post = Post.objects.create(
            title='Test Post', slug='test-post', author=self.user,
            content='This is a test post content.', excerpt='Test excerpt',
            status=1
        )

        # Check if the title, slug, author, and other fields are saved correctly
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.content, 'This is a test post content.')
        self.assertEqual(post.excerpt, 'Test excerpt')
        self.assertEqual(post.status, 1)

        # Test the number_of_likes method
        self.assertEqual(post.number_of_likes(), 0)

    def test_comment_model(self):
        # Create a post instance
        post = Post.objects.create(
            title='Test Post', slug='test-post', author=self.user,
            content='This is a test post content.', status=1
        )

        # Create a comment instance
        comment = Comment.objects.create(
            post=post, name='Test User', email='test@example.com',
            body='This is a test comment.'
        )

        # Check if the post, name, email, and other fields are saved correctly
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.name, 'Test User')
        self.assertEqual(comment.email, 'test@example.com')
        self.assertEqual(comment.body, 'This is a test comment.')
        self.assertFalse(comment.approved)

        # Test the __str__ method
        self.assertEqual(
            str(comment), f"Comment {comment.body} by {comment.name}"
        )
