# /bin/bash 

#
#Start Zookeeper Container
#
ZK_RUNNIING=$(docker inspect -f {{.State.Running}} zookeeper)
if [ "$ZK_RUNNIING" = "false" ]; then
    docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper
    if [ "$ZK_RUNNIING" = "false" ]; then
        docker start zookeeper
    fi
else
    printf "Zookeeper is already running\n"
fi

printf "Started Zookeeper Container...\n\n"

#
#Start Kafka Container
#
KAFKA_RUNNING=$(docker inspect -f {{.State.Running}} kafka)
if [ "$KAFKA_RUNNING" = "false" ]; then
    docker run -d -p 9092:9092 -e KAFKA_ADVERTISE_NAME=kafka -e KAFKA_ADVERTISE_PORT=9092 --name kafka  --link zookeeper:zookeeper confluent/kafka
    if [ "$KAFKA_RUNNING" = "false" ]; then
        docker start kafka
    fi
else
    printf "Kafka is already running\n"
fi

printf "Started Kafka Container...\n\n"

#
#setup and configure topic named "topic"
#
./../kafka_2.11-0.10.0.1/bin/kafka-topics.sh --create --if-not-exists  --zookeeper localhost --replication-factor 1 --partitions 1 --topic stock 

