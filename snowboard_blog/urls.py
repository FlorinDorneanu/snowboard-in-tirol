# * Import the necessary module from Django *
from . import views
from django.urls import path

# * Define urls patterns *
urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('comment/<int:comment_id>/like/',
         views.CommentLike.as_view(), name='comment_like'),
    path('<slug:slug>/<int:pk>/delete_comment/',
         views.CommentDelete.as_view(), name="delete_comment"),
    path('<slug:slug>/<int:pk>/edit_comment/',
         views.CommentEdit.as_view(), name="edit_comment"),
]
