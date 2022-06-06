#!/bin/bash
docker build -f Dockerfile.writing -t write-tweets .
docker run --network hw-kafka-network --rm write-tweets