from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib import admin
from snowboard_blog.views import PostList
from django_summernote.urls import urlpatterns as summernote_urls
from allauth.urls import urlpatterns as allauth_urls


class UrlsTestCase(SimpleTestCase):
    def test_admin_url(self):
        # Test URL pattern for the admin site
        url = reverse('admin:index')
        self.assertEqual(resolve(url).func, admin.site.urls)

    def test_home_url(self):
        # Test URL pattern for the home page
        url = reverse('snowboard_blog-urls:home')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_summernote_url(self):
        # Test URL pattern for the Summernote editor
        url = reverse('django_summernote:editor')
        self.assertIn(url, [str(pattern.pattern)
                      for pattern in summernote_urls])

    def test_allauth_urls(self):
        # Test URL patterns for Allauth authentication views
        for pattern in allauth_urls:
            url = reverse(pattern.name)
            self.assertIn(url, [str(pattern.pattern)
                          for pattern in allauth_urls])
