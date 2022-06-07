#!/bin/bash
docker build -f Dockerfile.reading -t from-kafka:1.0 .
docker run --rm --network hw-kafka-network -v --rm from-kafka:1.0