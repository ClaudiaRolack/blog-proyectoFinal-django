from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import SearchForm, CategoryForm, PostForm, CommentForm
from .models import Post, Category
from django.contrib.auth.decorators import login_required


@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Category.objects.filter(name__iexact=name).exists():
                messages.warning(request, f"La categoría '{name}' ya existe.")
            else:
                form.save()
                messages.success(request, f"Categoría '{name}' creada exitosamente.")
                return redirect('blog:create_category')
    else:
        form = CategoryForm()

    return render(request, 'blog/create_category.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, "Post creado exitosamente.")
            return redirect('blog:create_post')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-date')
    return render(request, 'blog/my_posts.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-date') 

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comentario publicado exitosamente.")
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

def search_post(request):
    form = SearchForm(request.GET or None)
    results = Post.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(categories__name__icontains=query)
            ).distinct()

    return render(request, 'blog/search.html', {
        'form': form,
        'results': results
    })