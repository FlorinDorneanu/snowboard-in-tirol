from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        reply_forms = []

        for comment in comments:
            comment_replies = comment.replies.filter(approved=False)

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
                "comment_form": CommentForm(initial={'parent_id': None}),
                "reply_forms": reply_forms,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        # if comment_form.is_valid():
        parent_id = comment_form.cleaned_data.get('parent_id')
        parent_comment = None

        if parent_id:
            try:
                parent_comment = Comment.objects.get(
                    id=parent_id, post=post, approved=True)
            except Comment.DoesNotExist:
                pass

            new_comment = Comment.objects.create(
                id=parend_id, post=post, approved=True)

            if parent_comment:
                new_comment.parent = parent_comment
                new_comment.approved_by_admin = False
                new_comment.save()
                parent_comment.replies.add(new_comment)
                return redirect(post.get_absolute_url())
                new_comment.approved_by_admin = False

            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form,
                "reply_forms": reply_forms,
            },
        )
