FROM python:3.11

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.app:app", "0.0.0.0", "--port", "5555"]