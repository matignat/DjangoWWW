from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import CommentForm
from django.db.models import Prefetch
from django.db.models import Count
from django.db.models import F
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PostForm

def post_list(request):
    posts = Post.objects.select_related("category")
    categories = Category.objects.all()
    return render(request, "blog/post_list.html", {
        "posts": posts, "categories": categories,
    })

def post_detail(request, slug):
    active_comments = Comment.objects.filter(active=True)

    post = get_object_or_404(
        Post.objects.prefetch_related(
            Prefetch("comments", queryset=active_comments, to_attr="active_comments")
        ),
        slug=slug,
    )

    if request.method == "GET":
        Post.objects.filter(pk=post.pk).update(view_count=F("view_count") + 1)
        post.refresh_from_db(fields=["view_count"])

    comments = post.active_comments
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", slug=post.slug)

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form,
    })

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    return render(request, "blog/post_list.html", {
        "posts": posts,
        "categories": Category.objects.all(),
        "active_category": category,
    })

@login_required
@user_passes_test(lambda u: u.is_staff)
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog:post-detail", slug=post.slug)
    else:
        form = PostForm()

    return render(request, "blog/post_create.html", {"form": form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("blog:post-detail", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_create.html", {"form": form, "post": post})