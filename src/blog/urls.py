from django.urls import path
from . import views
from .views import PostDetailView, MyPostsListView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('create_category/', views.create_category, name='create_category'),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('my_posts/', MyPostsListView.as_view(), name='my_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('search/', views.search_post, name='search'),
]