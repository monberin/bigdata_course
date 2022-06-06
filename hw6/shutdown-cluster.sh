#!/bin/bash
docker kill zookeeper-server
docker kill kafka-server
docker network rm hw-kafka-network