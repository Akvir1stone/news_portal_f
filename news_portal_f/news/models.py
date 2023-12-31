from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Authors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def update_rating(self):
        posts_rating_sum = 0
        comments_rating_sum = 0
        comments_on_posts_rating_sum = 0
        posts_rating = Post.objects.filter(author=self).values('rating')
        posts = Post.objects.filter(author=self)
        for i in posts_rating:
            for j in i.values():
                posts_rating_sum += j
        comments_rating = Comment.objects.filter(user=self.user).values('rating')
        for i in comments_rating:
            for j in i.values():
                comments_rating_sum += j
        for z in posts:
            comments_on_posts = Comment.objects.filter(at_post=z).values('rating')
            for i in comments_on_posts:
                for j in i.values():
                    comments_on_posts_rating_sum += j
        self.rating = posts_rating_sum*3 + comments_rating_sum + comments_on_posts_rating_sum
        self.save()


class Category(models.Model):
    CatName = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    articleORnews = models.BooleanField()  # article true / news false
    date_time = models.DateTimeField(auto_now_add=True)
    m_to_m_cat = models.ManyToManyField(Category, through="PostCategory")
    name = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField()

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

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
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
