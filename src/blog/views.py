from django.shortcuts import render
from forms import SearchForm
from .models import Post


def search_post(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/search.html', {'form': form, 'results': results})
