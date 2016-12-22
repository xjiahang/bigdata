#!/usr/bin/python 

from kafka import KafkaConsumer

if __name__ == "__main__":
    consumer = KafkaConsumer("stock");
    for message in consumer:
        print("topic : %s, message value %s" % (message.topic, message.value))
