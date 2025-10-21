FROM python:3.11-slim
WORKDIR /app
COPY app/ .  # ✅ copies contents of app/ into /app
RUN pip install -r requirements.txt
ENV FLASK_PORT=8000
CMD ["python", "app.py"]
