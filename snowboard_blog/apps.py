# * Import the necessary module from Django *
from django.apps import AppConfig


# * Define configuration class for snowboard blog app *
class SnowboardBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'snowboard_blog'
