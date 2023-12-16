from django.contrib.auth.models import User
from news.models import Authors
from news.models import Category
from news.models import Post
from news.models import Comment

user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')
user1.save()
user2.save()

author1 = Authors.objects.create(user=user1, rating=0)
author2 = Authors.objects.create(user=user2, rating=0)
author1.save()
author2.save()

cat1 = Category.objects.create(CatName='cat1')
cat2 = Category.objects.create(CatName='cat2')
cat3 = Category.objects.create(CatName='cat3')
cat4 = Category.objects.create(CatName='cat4')
cat1.save()
cat2.save()
cat3.save()
cat4.save()

post1 = Post.objects.create(articleORnews=True, rating=0, author=author1)
post2 = Post.objects.create(articleORnews=True, rating=0, author=author2)
post3 = Post.objects.create(articleORnews=False, rating=0, author=author1)
post1.save()
post2.save()
post3.save()
post1.m_to_m_cat.add(cat1, cat2)
post2.m_to_m_cat.add(cat3)
post3.m_to_m_cat.add(cat4)
post1.save()
post2.save()
post3.save()

com1 = Comment.objects.create(at_post=post1, user=user1, rating=0)
com2 = Comment.objects.create(at_post=post1, user=user2, rating=0)
com3 = Comment.objects.create(at_post=post2, user=user1, rating=0)
com4 = Comment.objects.create(at_post=post3, user=user1, rating=0)
com1.save()
com2.save()
com3.save()
com4.save()

post1.like()
post1.like()
post1.like()
post1.dislike()
post2.like()
post3.like()
com1.like()
com2.like()
com3.like()
com4.like()
