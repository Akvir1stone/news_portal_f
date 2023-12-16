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

author1.update_rating()
author2.update_rating()

best = [Authors.objects.all().order_by('-rating').values('user__username')[0].get('user__username'),
        Authors.objects.all().order_by('-rating').values('rating')[0].get('rating')]
print(f'Best user is: {best[0]}, with rating: {best[1]}')

post1.text = 'ajhdgfkjsahfkahglkjdahglkajgkajdlfdshjfljshdlfkahsdjfhakgakhgfkasdhgfkajdshgfkjdshgfksajhgfkjhsgdfkjhagdsfkjhgdfkjhagdfkjahgdfkahdjgfkdsajhgfkdsajh'
post1.name = 'name of post1'

best_com = [Post.objects.all().order_by('-rating').values('author__user__username')[0].get('author__user__username'),
            str(Post.objects.all().order_by('-rating').values('date_time')[0].get('date_time').date()),
            Post.objects.all().order_by('-rating').values('rating')[0].get('rating'),
            Post.objects.all().order_by('-rating').values('name')[0].get('name')]
print(f'Best comment author: {best_com[0]}, date: {best_com[1]}, rating: {best_com[2]}, name: {best_com[3]}, there is preview:')
print(Post.objects.all().order_by('-rating')[0].preview())
