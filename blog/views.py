from rest_framework.generics import (ListAPIView, CreateAPIView,
                                     RetrieveAPIView,
                                     ListCreateAPIView)
from .models import *
from .serializers import *


# Create your views here.


class HomeView(ListAPIView):
    queryset = Post.objects.all().order_by('created_at')[:7]
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ArticleView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AboutView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
