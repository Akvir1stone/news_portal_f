from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Authors, Category, Post, PostCategory, Comment
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = NewsForm()
        return context


class CreateNews(CreateView):
    template_name = 'CreateNews.html'
    form_class = NewsForm


class NewsSearch(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'NewsSearch.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = NewsForm()
        return context


class PostView(DetailView):
    template_name = 'PostTmplt.html'
    queryset = Post.objects.all()


class PostEdit(UpdateView):
    template_name = 'CreateNews.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'PostDelete.html'
    queryset = Post.objects.all()
    success_url = '/news'
