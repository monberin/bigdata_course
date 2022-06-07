#!/bin/bash
docker build -t run-transactions .
docker run --rm --network hw-kafka-network --rm run-transactions --name transactions