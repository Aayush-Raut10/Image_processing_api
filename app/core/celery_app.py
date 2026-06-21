import time
from celery import Celery
from app.core.config  import settings

# Connect to Redis broker and result backend
celery_app = Celery(
    "worker", 
    broker = settings.REDIS_URL, 
    backend = settings.REDIS_URL,
    include=["app.worker.image_tasks"]
)

celery_app.conf.update(
    
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
)

