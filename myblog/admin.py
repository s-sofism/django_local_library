from django.contrib import admin
from .models import Comment, Post, Tag


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['author', 'image', 'created_on', 'tags', 'content', 'title']


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ['post', 'author', 'text', 'created_on']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

