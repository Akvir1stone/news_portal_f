from django.db import models
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm
from django import forms
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from news_portal_f.settings import SITE_URL, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

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
    subs = models.ManyToManyField(User, related_name='cats')

    def __str__(self):
        return self.CatName


class Post(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    articleORnews = models.BooleanField()  # article true / news false
    date_time = models.DateTimeField(auto_now_add=True)
    m_to_m_cat = models.ManyToManyField(Category, through="PostCategory")
    name = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if not self.text:
            return 'No text'
        else:
            return self.text[:50] + '...'

    def self_name(self):
        if not self.name:
            return 'No name'
        else:
            return self.name

    def __str__(self):
        return f'{self.name}: {self.text[:20]}...'

    def detail(self):
        return f'{self.name}, {self.text}, {self.rating}, {self.author}, {self.date_time}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


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


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        usere = user.email
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)

        send_mail(
            subject='Добро',
            message=f'{SITE_URL}/news/',
            from_email=f'{EMAIL_HOST_USER}@yandex.ru',
            recipient_list=[usere],
        )

        return user


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    nick = forms.CharField(label="Имя")

    class Meta:
        model = User
        fields = ("username",
                  "nick",
                  "email",
                  "password1",
                  "password2", )
