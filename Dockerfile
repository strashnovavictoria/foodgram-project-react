FROM python:3.7

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . ./

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]