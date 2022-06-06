#!/bin/bash
docker build -f Dockerfile.reading -t read-tweets:1.0 .
docker run --network hw-kafka-network -v /home/monberin/Documents/bigdata/hw7:/hw7 --rm read-tweets:1.0