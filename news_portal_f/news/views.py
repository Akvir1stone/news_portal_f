from django.views.generic import ListView, DetailView
from .models import Authors, Category, Post, PostCategory, Comment
from .filters import NewsFilter


class NewsList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2


class NewsSearch(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'NewsSearch.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostView(DetailView):
    model = Post
    template_name = 'PostTmplt.html'
    context_object_name = 'post'
