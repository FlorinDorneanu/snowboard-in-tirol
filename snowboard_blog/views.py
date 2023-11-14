# * Import the necessary modules from Django *
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post, Comment
from .forms import CommentForm, EditForm


# * Define a class-based view for listing posts *

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


# * Define a class-based view for displaying post details
# and handling comments *

class PostDetail(SuccessMessageMixin, View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        liked_comments = comments.filter(likes__id=self.request.user.id)

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request,
                             'Your comment has been uploaded for approval.')
            comment_form = CommentForm()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "liked_comments": liked_comments
            },
        )


# * Define a class-based view for displaying post details
# and handling post likes *

class PostLike(LoginRequiredMixin, View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# * Define a class-based view for displaying post details
# and handling comments likes *

class CommentLike(View):

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)

        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[comment.post.slug]))


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    If user is logged in:
    Direct user to delete_comment.html template
    User will be prompted with a message to confirm deletion.
    """
    model = Comment
    template_name = "delete_comment.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user.username == comment.name

    def delete(self, request, *args, **kwargs):
        return super(CommentDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        PostDetail.comment_deleted = True
        messages.success(self.request, 'Your comment has been deleted.')
        return reverse("post_detail", kwargs={"slug": self.object.post.slug})


class CommentEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    If user is logged in:
    Direct user to update_comment.html template,
    displaying ReviewForm for that specific review.
    Post edited info back to the database and return user to post.
    """
    model = Comment
    form_class = EditForm
    template_name = "edit_comment.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user.username == comment.name

    def form_valid(self, form):
        """
        Upon success prompt the user with a success message.
        """
        super().form_valid(form)
        messages.success(self.request, 'Your comment has been edited.')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        """
        Upon success returns user to the post detail page.
        """
        PostDetail.comment_edited = True
        return reverse("post_detail", kwargs={"slug": self.object.post.slug})
