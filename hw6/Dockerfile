FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install kafka-python

WORKDIR /hw6
COPY ./reading_tweets.py .
COPY ./sample.csv .
ENTRYPOINT ["python", "reading_tweets.py"]
