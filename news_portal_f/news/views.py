from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Authors, Category, Post, PostCategory, Comment
from django.core.paginator import Paginator


class NewsList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2


class PostView(DetailView):
    model = Post
    template_name = 'PostTmplt.html'
    context_object_name = 'post'
