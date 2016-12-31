#! /bin/bash 
APP_NAME=$1
TOPIC_NAME=$2

spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.0.0.jar stock_process.py master $APP_NAME $TOPIC_NAME localhost:9092
