#!/bin/bash
docker build -f Dockerfile -t rest_api .
docker run --rm --network hw-kafka-network -v --rm rest_api