from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SearchForm, CategoryForm, PostForm, CommentForm
from .models import Post, Category, Comment


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date')
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog:create_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post creado exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ocurrió un error al guardar el post.")
        return super().form_invalid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-date')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"/login/?next={request.path}")

        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
            return redirect(self.request.path)

        context = self.get_context_data(object=self.object)
        context['form'] = form
        return self.render_to_response(context)
    
class MyPostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/my_posts.html'
    context_object_name = 'posts'
    ordering = ['-date']

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'
    success_url = reverse_lazy('blog:my_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:my_posts')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user 
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def form_valid(self, form):
        messages.success(self.request, "Comentario actualizado exitosamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        return self.get_object().author == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        return self.get_object().author == self.request.user

class PostsByCategoryListView(ListView):
    model = Post
    template_name = 'blog/posts_by_category.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return Post.objects.filter(categories__id=category_id).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            category = Category.objects.get(pk=self.kwargs.get('pk'))
        except Category.DoesNotExist:
            raise Http404("La categoría no existe.")
        context['category'] = category
        return context
    
@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Category.objects.filter(name__iexact=name).exists():
                messages.warning(request, f"La categoría '{name}' ya existe.")
            else:
                try:
                    form.save()
                    messages.success(request, f"Categoría '{name}' creada exitosamente.")
                    return redirect('blog:create_category')
                except Exception as e:
                    messages.error(request, f"Error al crear la categoría: {str(e)}")
    else:
        form = CategoryForm()

    return render(request, 'blog/create_category.html', {'form': form})

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

class AboutView(TemplateView):
    template_name = 'blog/about.html'