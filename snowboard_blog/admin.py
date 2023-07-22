from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from django.db import models
from django.forms import Textarea
from django_summernote.widgets import SummernoteWidget
from django import forms


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


class CommentAdminForm(forms.ModelForm):
    reply = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Comment
        fields = '__all__'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    form = CommentAdminForm
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments',
               'delete_comments', 'admin_reply_to_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def admin_reply_to_comments(self, modeladmin, request, queryset):
        for comment in queryset:
            comment.reply = "Admin reply"
            comment.save()
