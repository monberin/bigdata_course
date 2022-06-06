#!/bin/bash
docker build -t run-tweets .
docker run --name kafka-producer --network hw-kafka-network --rm run-tweets