FROM python:3.6-alpine3.6
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
CMD ["python", "backend_dev_app.py"]