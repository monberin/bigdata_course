#!/bin/bash
docker stop zookeeper-server kafka-server
docker rm zookeeper-server kafka-server
docker network rm hw-kafka-network