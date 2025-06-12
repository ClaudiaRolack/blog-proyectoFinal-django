from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create_category/', views.create_category, name='create_category'),
    path('create_post/', views.create_post, name='create_post'),
    path('my_posts', views.my_posts, name='my_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]