from fastapi import APIRouter, HTTPException, Depends, status

router = APIRouter(prefix="/api/v1/process")


@router.post("/")
def process_image():
    return "aa"