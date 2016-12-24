#!/usr/bin/python 

from kafka import KafkaConsumer
from cassandra.driver import Cluster
import argparse

def store_data(session, message):



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('kafka_url', help = 'kafka broker url')
    parser.add_argument('topic', help = 'topic name that consumer subscribes and table name')
    parser.add_argument('key_space', help = 'keyspace of cassandra'
    args = parser.parse_args()

#  start and connect cassandra cluster
   cluster = Cluster("localhost")
   session = cluster.connect()

#  create cassandra keyspace and table
   create_space = "CREATE KEYSPACE IF NOT EXISTS %s WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' :  1 } AND durable_writes = 'true'" % args.(key_space)
   session.execute(create_space)
   create_table = "CREATE TABLE IF NOT EXISTS %s (stock_symbol text, trade_time timestamp, trade_price float, PRIMARY KEY(stock_symbol, trade_time))" %s (args.topic)
   sesson.execute(create_table) 
   consumer = KafkaConsumer(args.topic, bootstrap_servers = [args.kafka_url])
   for message in consumer:
        print("topic : %s, message value %s" % (message.topic, message.value))
