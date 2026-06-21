from app.core.celery_app import celery_app

@celery_app.task(name="image_processing_task")
def image_processing_task(x:int, y:int):

    
    return x+y