from django.urls import path, include
from .views import NewsList, PostView, NewsSearch, CreateNews, PostEdit, PostDelete, Login


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', PostView.as_view(), name='post_detail'),
   path('search', NewsSearch.as_view(), name='post_search'),
   path('add', CreateNews.as_view(), name='post_add'),
   path('<int:pk>/edit', PostEdit.as_view(), name='post_update'),
   path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
]
