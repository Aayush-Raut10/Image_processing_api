from dotenv import load_dotenv
import os

class Settings():

    PROJECT_NAME = "Image Processing API"

    REDIS_URL = os.getenv("REDIS_URL")
    DATABASE_URL = os.getenv("DATABASE_URL")
    
    UPLOAD_DIR = "app/static/uploaded"
    PROCESSED_DIR = "app/static/processed"


settings = Settings()