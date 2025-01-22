FROM python:3.12

WORKDIR /app

RUN pip install pytest psycopg2-binary

COPY . .

CMD ["pytest"]
