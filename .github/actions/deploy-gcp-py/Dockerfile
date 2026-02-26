FROM python:3.11-slim

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY deploy.py /deploy.py

CMD ["python", "/deploy.py"]