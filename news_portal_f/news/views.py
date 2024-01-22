from django.shortcuts import render
from django.views.generic import ListView
from .models import Authors, Category, Post, PostCategory, Comment


class NewsList(ListView):
    model = Post
    ordering = 'date_time'
    template_name = 'news.html'
    context_object_name = 'news'

