from fastapi import APIRouter,UploadFile, File, Form, HTTPException, Depends, status
import json
from app.worker.image_tasks import image_processing_task
from app.services.file_service import save_image

router = APIRouter(prefix="/api/v1/images")


@router.post("/")
def process_image(file:UploadFile = File(...), operations:str = Form(...)):
    
    operations = json.loads(operations)

    file_path = save_image(file)
    
    task = image_processing_task.delay(file_path, operations)

    return {
        "task_id": task.id,
        "status": "PENDING",
        "message": "Image processing started",
        "created_at": "2026-06-21T16:30:00Z"
    }


