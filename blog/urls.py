from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('articles/', ArticleView.as_view(), name='articles'),
    path('articles/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('articles/<int:pk>/comments', CommentView.as_view(), name='comments')
]
