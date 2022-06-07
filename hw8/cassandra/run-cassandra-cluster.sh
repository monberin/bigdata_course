#!/bin/bash

docker run --name cassandra-server --network hw-kafka-network -p 9042:9042 -d cassandra:latest
sleep 90
docker cp /home/monberin/Documents/bigdata/hw8/cassandra/ddl-script.cql cassandra-server:/
docker exec -it cassandra-server cqlsh -f ddl-script.cql
