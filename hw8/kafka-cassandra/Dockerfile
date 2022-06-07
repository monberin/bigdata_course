FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install kafka-python
RUN pip install cassandra-driver
RUN pip install flask
WORKDIR /hw8/kafka-cassandra
COPY ./from_kafka.py .
COPY ./rest.py .
ENTRYPOINT ["python", "rest.py"]
