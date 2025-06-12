from django import forms
from .models import Category, Post, Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        widgets = {'categories': forms.CheckboxSelectMultiple()}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe un comentario...'})}

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=False)