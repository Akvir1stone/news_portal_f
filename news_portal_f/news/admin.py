from django.contrib import admin
from news.models import Authors, Category, Post, PostCategory, Comment


admin.site.register(Authors)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

# Register your models here.
