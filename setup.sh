#! /bin/bash 

#
#Start Zookeeper Container
#
ZK_RUNNIING=$(docker inspect -f {{.State.Running}} zookeeper)
if [ $? -eq 1 ]; then
    echo "Zookeeper container does not exist"
    docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper
fi

if [ "$ZK_RUNNIING" = "false" ]; then
    docker start zookeeper
fi

echo "Start to run Zookeeper"
sleep 5

#
#Start Kafka Container
#
KAFKA_RUNNING=$(docker inspect -f {{.State.Running}} kafka)
if [ $? -eq 1 ]; then
    echo "Kafka container does not exist"
    docker run -d -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME='localhost' -e KAFKA_ADVERTISED_PORT=9092 --name kafka  --link zookeeper:zookeeper confluent/kafka
fi

if [ "$KAFKA_RUNNING" = "false" ]; then
    docker start kafka
fi

echo "Start to run Kafka"

#
#setup and configure topic named "topic"
#

sleep 5

./../kafka_2.11-0.10.0.1/bin/kafka-topics.sh --create --if-not-exists  --zookeeper localhost --replication-factor 1 --partitions 1 --topic stock 

sleep 2

#
#Start Cassandra Container
#
CASSANDRA_RUNNIING=$(docker inspect -f {{.State.Running}} cassandra)
if [ $? -eq 1 ]; then
    echo "Cassandra container does not exist"
    docker run -d -p 7001:7001 -p 7199:7199 -p 9042:9042 -p 9160:9160 --name cassandra cassandra
fi

if [ "$CASSANDRA_RUNNIING" = "false" ]; then
        docker start cassandra
fi

echo "Start to run Cassandra"

#
#Start Redis Container
#
REDIS_RUNNIING=$(docker inspect -f {{.State.Running}} redis)
if [ $? -eq 1 ]; then
    echo "Redis container does not exist"
    docker run -d -p 6379:6379 --name redis redis
fi

if [ "$REDIS_RUNNIING" = "false" ]; then
        docker start redis
fi

echo "Start to run Redis"

