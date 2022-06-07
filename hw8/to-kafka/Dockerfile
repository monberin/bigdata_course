FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install kafka-python

WORKDIR /hw8
COPY writing_transactions.py .
COPY ../sample.csv .
ENTRYPOINT ["python", "writing_transactions.py"]
