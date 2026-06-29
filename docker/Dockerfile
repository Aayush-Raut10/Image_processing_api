FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

COPY  requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]