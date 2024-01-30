from django.urls import path
from .views import NewsList, PostView, NewsSearch


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', PostView.as_view()),
   path('search', NewsSearch.as_view()),
]
