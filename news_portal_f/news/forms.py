from django.forms import ModelForm
from .models import Authors, Category, Post, PostCategory, Comment


class NewsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'author', 'articleORnews', 'm_to_m_cat', 'text']
