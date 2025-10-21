FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r app/requirements.txt
ENV FLASK_PORT=8000
CMD ["python", "app.py"]
