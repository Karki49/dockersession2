FROM python:3.6-alpine3.6
WORKDIR /code
COPY . /code
CMD ["python", "batch.py"]