from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from news_portal_f.settings import SITE_URL, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from .models import PostCategory



def send_note(preview, pk, title, subs):
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


@receiver(m2m_changed, sender=PostCategory)
def notify_ab_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        cats = instance.m_to_m_cat.all()
        subs: list[str] = []
        for cat in cats:
            subs += cat.subs.all()

        subs = [s.email for s in subs]

        send_note(instance.preview(), instance.pk, instance.name, subs)
