from django import forms
from .models import Comment
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'body')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'title', 'post')
