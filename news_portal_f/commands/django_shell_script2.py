best = [Authors.objects.all().order_by('-rating').values('user__username')[0].get('user__username'),
        Authors.objects.all().order_by('-rating').values('rating')[0].get('rating')]
print(f'Best user is: {best[0]}, with rating: {best[1]}')



best_com = [Post.objects.all().order_by('-rating').values('author__user__username')[0].get('author__user__username'),
            str(Post.objects.all().order_by('-rating').values('date_time')[0].get('date_time').date()),
            Post.objects.all().order_by('-rating').values('rating')[0].get('rating'),
            Post.objects.all().order_by('-rating').values('name')[0].get('name')]
print(f'Best comment author: {best_com[0]}, date: {best_com[1]}, rating: {best_com[2]}, name: {best_com[3]}, there is preview:')
print(Post.objects.all().order_by('-rating')[0].preview())

str(Comment.objects.filter(at_post=post1).values('date_time')[0].get('date_time').date())

com_at_post1 = []

for i in range(len(Comment.objects.filter(at_post=post1))):
    com_at_post1.append([str(Comment.objects.filter(at_post=post1).values('date_time')[i].get('date_time').date()),
                         Comment.objects.filter(at_post=post1).values('user__username')[i].get('user__username'),
                         Comment.objects.filter(at_post=post1).values('rating')[i].get('rating'),
                         Comment.objects.filter(at_post=post1).values('c_text')[i].get('c_text')])

for i in range(len(Comment.objects.filter(at_post=post1))):
    print(f'Date: {com_at_post1[i][0]}, user: {com_at_post1[i][1]}, rating: {com_at_post1[i][2]}, text: {com_at_post1[i][3]}')
