import os
from celery import Celery

# comment this env variables for docker-compose.yml
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('final_project_celery')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'ret_any_sum': {
#         'task': 'tasks.ret_sum',
#         'schedule': 2,
#         'args': (16, 16),
#     },
# }
