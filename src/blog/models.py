from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length = 150, unique=True)

    def __str__(self):
        return self.name
    
    def Meta():
        pass

class Post(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'posts')
    categories = models.ManyToManyField(Category, related_name = 'posts')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'comments')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name= 'comments')

    def __str__(self):
        return f"Comentario de {self.author.username} en {self.post.title}"