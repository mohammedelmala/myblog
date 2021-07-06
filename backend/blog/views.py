from django.shortcuts import render
from rest_framework.response import Response
from .models import Tag, Author, Post
from .serializers import TagSerializer, AuthorSerializer, PostSerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(["GET"])
def tags_view(request):
    tags = Author.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def authors_view(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def posts_view(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
