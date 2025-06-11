from django import forms
from .models import Category, Post, Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date', 'author','categories']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'date', 'author', 'post']

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)