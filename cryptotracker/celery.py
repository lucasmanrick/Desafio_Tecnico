# cryptotracker/celery.py
import os
from celery import Celery

# Ajuste aqui para o nome do seu project (pasta que contém settings.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptotracker.settings')

app = Celery('cryptotracker')

# Faz com que o Celery leia variáveis com prefixo CELERY_ do settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre tasks em apps listados em INSTALLED_APPS (procura tasks.py)
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')