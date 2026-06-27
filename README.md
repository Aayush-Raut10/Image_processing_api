## Image Processing API

A scalable image processing API built with FastAPI, Celery, and Redis. The API allows users to upload images, process them asynchronously, and track task status in real-time.

## Features
- Upload images through REST API
- Asynchronous image processing using Celery
- Redis-backed task queue
- Background processing for long-running tasks
- Task status tracking
- Image download support
- Static file serving
- Interactive API documentation with Swagger UI
- Modular FastAPI project structure

## Tech Stack
- Backend
    - FastAPI

- Queue System 
    - Celery (worker)
    - Redis (Message broker)


## Installation

### 1. Clone the Repository 

```bash 
git clone https://github.com/Aayush-Raut10/Image_processing_api.git
cd Image_processing_api
```

### 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```
### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### Running the Application

#### Step 1: Start Redis

Make sure your Redis server is running before starting the application.

#### Step 2: Start the Celery Worker
Open a new terminal and run:
```bash
celery -A app.celery_app.celery worker --pool=solo --loglevel=info
```

#### Step 3: Start the FastAPI Server
Open another terminal and run:
```bash
uvicorn app.main:app --reload
```

### 7. Open the API Documentation

After the server starts, open your browser and visit:

- **API:**  http://127.0.0.1:8000
- **Swagger UI:**  http://127.0.0.1:8000/docs
- **ReDoc:**  http://127.0.0.1:8000/redoc