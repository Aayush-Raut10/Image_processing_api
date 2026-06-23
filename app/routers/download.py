from fastapi import APIRouter
\
router = APIRouter(prefix="/api/v1")

from fastapi.responses import FileResponse
import os

@router.get("/download")
def download_file(path: str):

    return FileResponse(
        path=path,
        media_type="application/octet-stream",
        filename=os.path.basename(path)
    )