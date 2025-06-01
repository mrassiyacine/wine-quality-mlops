from python:3.12-slim

WORKDIR /app

COPY requirement.txt .
RUN pip install --upgrade pip && pip install -r requirement.txt

COPY . .
EXPOSE 8080

CMD ["python", "app.py"]