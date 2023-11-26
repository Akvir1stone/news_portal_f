from django.db import models

# Create your models here.


class Authors(models.Model):
    # TODO one to one User
    rating = models.IntegerField()

    def update_rating(self):
        pass


class Category(models.Model):
    CatName = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    # TODO one to many Author
    articleORnews = models.BooleanField()  # article true / news false # TODO try do without bool, but instead with char field
    date_time = models.DateTimeField(auto_now_add=True)
    m_to_m_cat = models.ManyToManyField(Category, through="PostCategory")
    name = models.CharField()
    text = models.TextField()
    rating = models.IntegerField()

    def like(self):
        pass

    def dislike(self):
        pass

    def preview(self):
        pass


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    at_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # TODO one to many user
    c_text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    def like(self):
        pass

    def dislike(self):
        pass

