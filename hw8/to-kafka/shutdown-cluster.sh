#!/bin/bash
docker stop zookeeper-server kafka-server cassandra-server
docker rm zookeeper-server kafka-server cassandra-server
docker network rm hw-kafka-network