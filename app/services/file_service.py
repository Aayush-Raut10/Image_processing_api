import os
from uuid import uuid4
from fastapi import UploadFile

UPLOAD_DIR = "static/uploaded"


def save_image(file: UploadFile) -> str:
    """
    Saves uploaded image to local storage and returns file path.
    """

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    filename = file.filename
    extension = os.path.splitext(filename)[1] 

    unique_name = f"{uuid4().hex}{extension}"

    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as buffer:
        while chunk := file.file.read(1024 * 1024):  
            buffer.write(chunk)

    return file_path