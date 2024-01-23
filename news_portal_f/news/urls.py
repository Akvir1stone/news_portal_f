from django.urls import path
from .views import NewsList, PostView


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', PostView.as_view()),
]
