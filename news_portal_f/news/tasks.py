from datetime import datetime, timedelta

from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from news_portal_f.settings import SITE_URL, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from .models import Post
from django.contrib.auth.models import User
import pytz


@shared_task
def send_note_task(pk):
    post = Post.objects.get(pk=pk)
    cats = post.m_to_m_cat.all()
    preview = post.preview()
    title = post.name
    subs = []

    for cat in cats:
        subsu = cat.subs.all()
        for s in subsu:
            subs.append(s.email)

    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=f'{EMAIL_HOST_USER}@yandex.ru',
        to=subs,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def weekly_task():
    posts = Post.objects.all()
    users = User.objects.all()
    user_emails = [u.email for u in users]
    # week_posts = []
    links = ''
    utc = pytz.UTC
    end = datetime.now()
    start = end - timedelta(days=7)

    for post in posts:
        if start.replace(tzinfo=utc) >= post.date_time.replace(tzinfo=utc) <= end.replace(tzinfo=utc):
            # week_posts.append(post)
            links = links + f'{SITE_URL}/news/{post.pk} {post.name}\n'

    html_content = render_to_string(
        'weekly_sent.html',
        {
            'text': links,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Новые статьи за неделю',
        body='',
        from_email=f'{EMAIL_HOST_USER}@yandex.ru',
        to=user_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
