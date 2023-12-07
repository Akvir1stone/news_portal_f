from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Authors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def update_rating(self):
        pass


class Category(models.Model):
    CatName = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    articleORnews = models.BooleanField()  # article true / news false # TODO try do without bool, but instead with char field
    date_time = models.DateTimeField(auto_now_add=True)
    m_to_m_cat = models.ManyToManyField(Category, through="PostCategory")
    name = models.CharField()
    text = models.TextField()
    rating = models.IntegerField()

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def preview(self):
        return self.text[:124:] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    at_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1
