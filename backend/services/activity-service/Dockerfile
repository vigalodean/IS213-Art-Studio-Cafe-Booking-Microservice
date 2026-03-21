FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY images ./images 

EXPOSE 8000

<<<<<<< Updated upstream
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> Stashed changes
