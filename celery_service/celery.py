from celery import Celery

from config import RABBITMQ_URL

celery_app = Celery(
    "pika",
    broker=RABBITMQ_URL,
    backend="rpc://",
    include=[
        "celery_service.tasks.fetch_countries",
    ]
)
celery_app.autodiscover_tasks()
