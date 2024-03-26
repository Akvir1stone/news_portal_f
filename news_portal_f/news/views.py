from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Authors, Category, Post, PostCategory, Comment, BaseRegisterForm
from .filters import NewsFilter
from .forms import NewsForm
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from .tasks import send_note_task
from django.core.cache import cache


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


class CreateNews(PermissionRequiredMixin, CreateView):
    model = Post
    permission_required = ('news.add_Post', 'news.change_Post')
    template_name = 'CreateNews.html'
    form_class = NewsForm

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.user = self.request.user

        post.save()
        send_note_task.delay(form.instance.pk)
        return super().form_valid(form)


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
        context['catsn'] = self.cats
        return context


# @cache_page(60*5)
class PostView(DetailView):
    template_name = 'PostTmplt.html'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'product-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'product-{self.kwargs["pk"]}', obj)
        return obj


class PostEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.add_Post', 'news.change_Post')
    template_name = 'CreateNews.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'PostDelete.html'
    queryset = Post.objects.all()
    success_url = '/news'


class Login(TemplateView):
    template_name = 'Login.html'
    success_url = '/news'


class UserPage(LoginRequiredMixin, TemplateView):
    template_name = 'UserPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/news'


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/news')


class CatList(ListView):
    model = Post
    template_name = 'CatList.html'
    context_object_name = 'catlists'

    def get_queryset(self):
        self.cats = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(m_to_m_cat=self.cats).order_by('-date_time')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_sub'] = self.request.user not in self.cats.subs.all()
        context['cat'] = self.cats
        return context


@login_required
def sub(request, pk):
    user = request.user
    cat = Category.objects.get(id=pk)
    cat.subs.add(user)
    mes = _('Подписан')
    return render(request, 'subbed.html', {'cat': cat, 'mes': mes})

