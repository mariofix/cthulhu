import os
from celery import Celery
import dotenv

dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

if os.getenv("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"] = os.getenv("DJANGO_SETTINGS_MODULE")

app = Celery("cthulhu")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
