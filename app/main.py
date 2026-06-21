from fastapi import FastAPI

app = FastAPI(title="Image processing API")


app.include_router()
