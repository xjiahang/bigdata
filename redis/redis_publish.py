#! /usr/bin/python 
# publish kafka records to redis channel

from kafka import KafkaConsumer
import redis
import argparse


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('kafka_topic', help = 'kafka topic name')
    args.add_argument('kafka_broker_url', help = 'kafka broker url')
    args.add_argument('redis_host', help = 'redis host')
    args.add_argument('redis_port', help = 'redis port')
    args.add_argument('redis_channel', help = 'redis channel')
    parser = args.parse_args()

    kafka_topic = parser.kafka_topic
    kafka_broker_url = parser.kafka_broker_url
    redis_host = parser.redis_host
    redis_port = parser.redis_port
    redis_channel = parser.redis_channel

    consumer = KafkaConsumer(kafka_topic, bootstrap_servers = [kafka_broker_url])
    redis_client = redis.StrictRedis(host = redis_host, port = redis_port, db = 0) 
    
    for message in consumer:
        print message.value
        redis_client.publish(redis_channel, message.value)   






