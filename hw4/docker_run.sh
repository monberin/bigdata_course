docker build . -t rest_cassandra
docker start node1
docker run --network hw-cassandra-network --rm rest_cassandra