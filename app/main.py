from fastapi import FastAPI
from app.routers import process, tasks, download
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="Image processing API")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)
from fastapi.staticfiles import StaticFiles

origins = [

     "https://image-process-frontend.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(process.router)
app.include_router(tasks.router)
app.include_router(download.router)
