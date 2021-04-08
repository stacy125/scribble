from django.contrib import admin

# Register your models here.

from .models import Post
from .models import Comment
from .form import PostForm
from .form import CommentForm


admin.site.register(Post)
admin.site.register(Comment)
