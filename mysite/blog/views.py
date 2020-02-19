from django.views import generic
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.utils import timezone


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    recent_posts = Post.objects.filter(
        created_on__lte=timezone.now()).order_by('-created_on')[:5]

    return render(request, 'post_detail.html', {'post': post, 'recent_posts':recent_posts})

def post_list(request):
    posts = Post.objects.filter(
            created_on__lte=timezone.now()).order_by('-created_on')
    recent_posts = Post.objects.filter(
        created_on__lte=timezone.now()).order_by('-created_on')[:7]

    return render(request, 'post_list.html', {'posts': posts, 'recent_posts': recent_posts})

def post_new(request):
    recent_posts = Post.objects.filter(
        created_on__lte=timezone.now()).order_by('-created_on')[:5]

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title, allow_unicode=True)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()

    return render(request, 'post_edit.html', {'form': form, 'recent_posts': recent_posts})

def post_edit(request, slug):
    recent_posts = Post.objects.filter(
    created_on__lte=timezone.now()).order_by('-created_on')[:5]
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title, allow_unicode=True)
        post.save()
        return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
        
    return render(request, 'post_edit.html', {'form': form, 'recent_posts': recent_posts})
