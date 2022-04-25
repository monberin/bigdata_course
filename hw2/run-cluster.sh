#!/bin/bash
docker network create hw-cassandra-network
docker run --rm --name node1 --network hw-cassandra-network -d cassandra:latest
sleep 60
docker run --rm --name node2 --network hw-cassandra-network -d -e CASSANDRA_SEEDS=node1 cassandra:latest
sleep 60
docker run --rm --name node3 --network hw-cassandra-network -d -e CASSANDRA_SEEDS=node1,node2 cassandra:latest
docker ps