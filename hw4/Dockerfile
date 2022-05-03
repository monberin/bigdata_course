FROM python:3.9-slim

RUN pip install --upgrade pip

RUN pip install cassandra-driver

RUN pip install flask
COPY ./read_from_cassandra.py /opt/app/
COPY ./rest.py /opt/app
ENTRYPOINT ["python", "/opt/app/rest.py"]
