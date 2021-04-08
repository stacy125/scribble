from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment
from .form import PostForm, CommentForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scrib/post_list.html', {'posts': posts})


def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'scrib/comment_list.html', {'comments': comments})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'scrib/post_detail.html', {'post': post})


def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'scrib/comment_detail.html', {'comment': comment})


def post_create(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'scrib/post_form.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
        else:
            return render(request, 'scrib/post_form.html', {'form': form})


def comment_create(request):
    if request.method == 'GET':
        form = CommentForm()
        return render(request, 'scrib/comment_form.html', {'form': form})
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
        else:
            return render(request, 'scrib/comment_form.html', {'form': form})


def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'scrib/post_form.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
            return render(request, 'scrib/post_form.html', {'form': form})


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('post_list')


def comment_edit(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == 'GET':
        form = CommentForm(instance=comment)
        return render(request, 'scrib/comment_form.html', {'form': form})
    elif request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            post = form.save()
            return redirect('comment_detail', pk=comment.pk)
        else:
            form = CommentForm(instance=comment)
            return render(request, 'scrib/comment_form.html', {'form': form})


def comment_delete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return redirect('comment_list')
