#!/bin/bash
docker network create hw-cassandra-network
docker run --name node1 --network hw-cassandra-network -p 9042:9042 -d cassandra:latest