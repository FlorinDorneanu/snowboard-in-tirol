# * Import the necessary module from Django *
from django.contrib import admin
from django.urls import path, include

# * Define urls patterns *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("snowboard_blog.urls"), name="snowboard_blog-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
]

handler404 = 'snowboard_in_tirol.views.handler404'
handler500 = 'snowboard_in_tirol.views.handler500'
handler403 = 'snowboard_in_tirol.views.handler403'
handler405 = 'snowboard_in_tirol.views.handler405'