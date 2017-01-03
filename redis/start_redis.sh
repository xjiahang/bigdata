#! /bin/bash

KAFKA_TOPIC=$1
REDIS_CHANNEL=$2
python redis_publish.py $KAFKA_TOPIC localhost:9092 localhost 6379 $REDIS_CHANNEL
