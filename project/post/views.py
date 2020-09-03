from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Post, Category, CategorySeries
from .forms import PostForm
from comment.forms import CommentForm
from django.contrib import messages

# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'post/category_list.html', context)

def category_series(request, single_slug):
    category = get_object_or_404(Category, category_slug=single_slug)
    series = [c for c in category.categories.all()]
    posts = []
    for s in series:
        for post in s.category_series.all():
            posts.append(post)
    context = {'category':category, 'post':posts[0]}
    return render(request, 'post/category_series.html', context)

def first_post(request, slug):
    series = get_object_or_404(CategorySeries, series_slug=slug)
    posts = [post for post in series.category_series.all()]
    context = {'posts':posts, 'first_page':posts[0]}
    return render(request, 'post/first_post.html', context)

def category_post(request, slug):

    post = get_object_or_404(Post, slug=slug)
    categories = Post.objects.filter(series__series_name=post.series)

    context = {'posts': categories, 'first_page': post}
    return render(request, 'post/category_post.html', context)

def post_detail(request, slug=None):
    post = get_object_or_404(CategorySeries, series_slug=slug)
    form = CommentForm(request.POST or None)
    
    if form.is_valid():
        comment_form = form.save(commit=False)
        comment_form.post = post
        comment_form.save()

        return HttpResponseRedirect(post.get_absolute_url())

    context = {'posts': post, 'comment_form': form}
    return render(request, 'post/post_detail.html', context)

def post_create(request):
    post = Post.objects.all()
    form = PostForm(request.POST or None)
    update = False
    if form.is_valid():
        save = form.save()
        messages.success(request, f'{save.title} is created!')
        return HttpResponseRedirect(save.get_absolute_url())

    context = {'form': form, 'update':update}
    return render(request, 'post/post_form.html', context)

def post_edit(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, instance=post)
    update = True
    if form.is_valid():
        save = form.save()
        return HttpResponseRedirect(save.get_absolute_url())
    context = {'form': form, 'post': post, 'update': update}
    return render(request, 'post/post_form.html', context)