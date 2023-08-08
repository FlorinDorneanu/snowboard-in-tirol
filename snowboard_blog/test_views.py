from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment
from .views import PostList, PostDetail, PostLike, CommentLike


class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.factory = RequestFactory()

    def test_post_list_view(self):
        # Create a request
        request = self.factory.get(reverse('home'))
        request.user = self.user

        # Test PostList view
        response = PostList.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        # Create a post instance
        post = Post.objects.create(
            title='Test Post', slug='test-post', author=self.user,
            content='This is a test post content.', status=1
        )

        # Create a request
        request = self.factory.get(reverse('post_detail', args=['test-post']))
        request.user = self.user

        # Test PostDetail view
        response = PostDetail.as_view()(request, slug='test-post')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_like_view(self):
        # Create a post instance
        post = Post.objects.create(
            title='Test Post', slug='test-post', author=self.user,
            content='This is a test post content.', status=1
        )

        # Create a request
        request = self.factory.post(reverse('post_like', args=['test-post']))
        request.user = self.user

        # Test PostLike view
        response = PostLike.as_view()(request, slug='test-post')
        self.assertEqual(response.status_code, 302)

    def test_comment_like_view(self):
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

        # Create a request
        request = self.factory.post(reverse('comment_like', args=[comment.id]))
        request.user = self.user

        # Test CommentLike view
        response = CommentLike.as_view()(request, comment_id=comment.id)
        self.assertEqual(response.status_code, 302)
