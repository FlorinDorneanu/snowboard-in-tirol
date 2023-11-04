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

handler404 = 'w_shop.views.handler404'
handler500 = 'w_shop.views.handler500'
handler403 = 'w_shop.views.handler403'
handler405 = 'w_shop.views.handler405'