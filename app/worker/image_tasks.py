from app.core.celery_app import celery_app
from typing import List
from app.services.image_service import resize_image, blur_image, grayscale_image, compress_image, create_thumbnail


@celery_app.task(name="image_processing_task")
def image_processing_task(file_path: str, operations: List[str]):

    results = []
    failed = 0

    for op in operations:

        if op.lower() == "resize":
            output_path = resize_image(file_path, width=100, height=400)
            output_path = output_path.replace("\\", "/")
            results.append({
                "operation": "resize",
                "output_path": output_path
            })

        elif op.lower() == "blur":
            output_path = blur_image(image_path=file_path)
            output_path = output_path.replace("\\", "/")
            results.append({
                "operation": "blur",
                "output_path": output_path
            })

        elif op.lower() == "compress":
            output_path = compress_image(image_path=file_path)
            output_path = output_path.replace("\\", "/")
            results.append({
                "operation": "compress",
                "output_path": output_path
            })

        elif op.lower() == "thumbnail":
            output_path = create_thumbnail(image_path=file_path)
            output_path = output_path.replace("\\", "/")
            results.append({
                "operation": "thumbnail",
                "output_path": output_path
            })

        else:
            failed += 1
            results.append({
                "operation": op,
                "status": "skipped",
                "reason": "unknown operation"
            })

    status = "SUCCESS" if failed == 0 else "PARTIAL_SUCCESS"

    return {
        "status": status,
        "file_path": file_path,
        "results": results
    }