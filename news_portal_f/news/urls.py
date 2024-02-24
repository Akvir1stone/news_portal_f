from django.urls import path
from .views import NewsList, PostView, NewsSearch, CreateNews, PostEdit, PostDelete, BaseRegisterView, upgrade_me, CatList, sub
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', NewsList.as_view(), name='main'),
   path('<int:pk>', PostView.as_view(), name='post_detail'),
   path('search', NewsSearch.as_view(), name='post_search'),
   path('add', CreateNews.as_view(), name='post_add'),
   path('<int:pk>/edit', PostEdit.as_view(), name='post_update'),
   path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
   path('login/', LoginView.as_view(template_name='auth_templates/login.html'), name='login_temp'),
   path('logout/', LogoutView.as_view(template_name='auth_templates/logout.html'), name='logout_temp'),
   path('signup/', BaseRegisterView.as_view(template_name='auth_templates/signup.html'), name='signup_temp'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('cats/<int:pk>', CatList.as_view(), name='catlist'),
   path('cats/<int:pk>/sub/', sub, name='subtocat'),
]
