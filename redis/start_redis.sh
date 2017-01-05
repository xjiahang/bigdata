#! /bin/bash

KAFKA_TOPIC=average-price
REDIS_CHANNEL=average-stock
python redis_publish.py $KAFKA_TOPIC localhost:9092 localhost 6379 $REDIS_CHANNEL
