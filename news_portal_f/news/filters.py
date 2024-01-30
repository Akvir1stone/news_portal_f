from django_filters import FilterSet
from .models import Authors, Category, Post, PostCategory, Comment


class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'name': ['icontains'],
                  'author': ['exact'],
                  'date_time': ['date__gt'],
                  'rating': ['gt']
                  }
