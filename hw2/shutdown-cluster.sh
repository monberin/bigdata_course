#!/bin/bash
docker kill node1
docker kill node2
docker kill node3
docker network rm hw-cassandra-network