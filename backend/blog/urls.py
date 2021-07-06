from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts_view, name="posts"),
    path('authors/', views.authors_view, name="authors"),
    path('tags/', views.tags_view, name="tags")
]
