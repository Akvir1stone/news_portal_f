from django.db import models

# Create your models here.


class Authors(models.Model):
    # one to one User
    # rating
    pass


class Category(models.Model):
    CatName = models.CharField(max_length=50, unique=True)
    pass


class Post(models.Model):
    # one to many Author
    articleORnews = models.BooleanField()  # article true / news false
    date_time = models.DateTimeField(auto_now_add=True)
    m_to_m_cat = models.ManyToManyField(Category, through="PostCategory")
    name = models.CharField()
    text = models.TextField()
    rating = models.IntegerField()
    pass


class PostCategory(models.Model):
    pass


class Comment(models.Model):
    pass

