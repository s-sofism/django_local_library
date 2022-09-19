from .models import Post, Tag, User
from asgiref.sync import sync_to_async


@sync_to_async()
def get_all_posts():
    return Post.objects.all()


@sync_to_async()
def get_post_detail():
    return Post.objects.all().order_by("-created_on")


@sync_to_async()
def get_all_available_posts():
    return Post.objects.filter(status='PUBLISH').order_by("-created_on")


@sync_to_async()
def get_all_users():
    return User.objects.all()


@sync_to_async()
def get_all_draft_posts():
    return Post.objects.filter(status='DRAFT').order_by("-created_on")


@sync_to_async()
def get_all_archived_posts():
    return Post.objects.filter(status='ARCHIVE').order_by("-created_on")