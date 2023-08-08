from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import PostList, PostDetail, PostLike, CommentLike


class UrlsTestCase(SimpleTestCase):
    def test_home_url(self):
        # Test URL pattern for the home page
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_post_detail_url(self):
        # Test URL pattern for the post detail page
        url = reverse('post_detail', args=['test-post'])
        self.assertEqual(resolve(url).func.view_class, PostDetail)

    def test_post_like_url(self):
        # Test URL pattern for liking a post
        url = reverse('post_like', args=['test-post'])
        self.assertEqual(resolve(url).func.view_class, PostLike)

    def test_comment_like_url(self):
        # Test URL pattern for liking a comment
        url = reverse('comment_like', args=[1])
        self.assertEqual(resolve(url).func.view_class, CommentLike)
