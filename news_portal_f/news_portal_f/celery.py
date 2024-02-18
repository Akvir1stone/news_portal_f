import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal_f.settings')

app = Celery('news')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'weekly_posts_update': {
        'task': 'news.tasks.weekly_task',
        'schedule': crontab(hour=5, minute=0, day_of_week='monday')
    }
}

app.conf.timezone = 'UTC'
