from django.db import models
from django.contrib.auth.models import User

STATUS = (
    ('DRAFT', "Draft"),
    ('PUBLISH', "Publish"),
    ('ARCHIVE', "Archive"),
)


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    content = models.TextField()
    status = models.CharField(max_length=64, choices=STATUS, default='DRAFT')
    image = models.ImageField(
        upload_to="post",
        default="post/sample.jpg",
    )
    author = models.ForeignKey(
        User,
        related_name="blog_posts",
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text



