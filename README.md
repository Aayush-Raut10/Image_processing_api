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
