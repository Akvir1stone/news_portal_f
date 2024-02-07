from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Authors, Category, Post, PostCategory, Comment, UserCat
from .filters import NewsFilter
from .forms import NewsForm
from .models import BaseRegisterForm
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


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
    permission_required = ('news.add_Post', 'news.change_Post')
    template_name = 'CreateNews.html'
    form_class = NewsForm

    def post(self, request, *args, **kwargs):
        sub = UserCat(
            user=self.User,
            cat=request.POST['m_to_m_cat'],
        )
        send_mail(
            f'{self.form_class["name"]}',

        )


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
