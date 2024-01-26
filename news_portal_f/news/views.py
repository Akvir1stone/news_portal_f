from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Authors, Category, Post, PostCategory, Comment


class NewsList(ListView):
    model = Post
    ordering = 'date_time'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostView(DetailView):
    model = Post
    template_name = 'PostTmplt.html'
    context_object_name = 'post'

