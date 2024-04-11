from django.contrib import admin
from .models import Authors, Category, Post, PostCategory, Comment
from modeltranslation.admin import TranslationAdmin


admin.site.register(Authors)
# admin.site.register(Category)
# admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

# Register your models here.

class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post


admin.site.register(Post)
admin.site.register(Category)
