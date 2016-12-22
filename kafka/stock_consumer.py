#!/usr/bin/python 

from kafka import KafkaConsumer
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('kafka_url', help = 'kafka broker url')
    parser.add_argument('topic', help = 'topic name that consumer subscribes')
    args = parser.parse_args()

    consumer = KafkaConsumer(args.topic, bootstrap_servers = [args.kafka_url])
    for message in consumer:
        print("topic : %s, message value %s" % (message.topic, message.value))
