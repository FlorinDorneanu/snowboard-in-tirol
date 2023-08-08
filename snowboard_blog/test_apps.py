from django.test import TestCase
from snowboard_blog.apps import SnowboardBlogConfig


class AppConfigTestCase(TestCase):
    def test_app_config(self):
        # Create an instance of SnowboardBlogConfig
        app_config = SnowboardBlogConfig()

        # Check if the app name is correct
        self.assertEqual(app_config.name, 'snowboard_blog')

        # Check if the default auto field is correctly set
        self.assertEqual(app_config.default_auto_field,
                         'django.db.models.BigAutoField')
