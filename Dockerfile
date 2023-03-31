FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV USERNAME developer
ENV PASSWORD Redecoygooglereissue

CMD ["python", "app.py"]
