from django import forms
from .models import Comment, Post, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("status", "created_on", "updated_on")
        tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control content"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "author": forms.HiddenInput,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "post",
            "author",
            "text",
        )
        widgets = {
            "post": forms.HiddenInput(),
            "author": forms.HiddenInput,
            "text": forms.Textarea(attrs={"class": "form-control content"}),
        }

