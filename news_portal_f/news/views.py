from django.shortcuts import render
from django.views.generic import ListView
from .news.models import Authors, Category, Post, PostCategory, Comment


class NewsList(Post):
    model = Post
    ordering = 'date_time'
    template_name = 'news.html'
    context_object_name = 'news'

