FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/ /app/src/

CMD ["python", "/app/src/controller.py"]
