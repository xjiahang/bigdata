#!/usr/bin/python 

from kafka import KafkaConsumer
from cassandra.driver import Cluster
import argparse
import json

def store_data(session, message):
    stock_info = json.loads(message.value)
    stock_symbol = stock_info[0]["StockSymbol"]
    stock_tradetime = stock_info[0]["LastTradeTime"]
    stock_tradeprice = float(stock_info[0]["LastTradePrice"])
    statement = "INSERT INTO stock (stock_symbol, trade_time, trade_price) VALUES (%s, %s, %f) % (stock_symbol, stock_tradetime, stock_tradeprice)"
    sesson.execute(statement)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('kafka_url', help = 'kafka broker url')
    parser.add_argument('topic', help = 'topic name that consumer subscribes and table name')
    parser.add_argument('key_space', help = 'keyspace of cassandra')
    args = parser.parse_args()

#  start and connect cassandra cluster
   cluster = Cluster("localhost")
   session = cluster.connect()

#  operate on cassandra table
   create_space = "CREATE KEYSPACE IF NOT EXISTS %s WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' :  1 } AND durable_writes = 'true'" % args.key_space)
   session.execute(create_space)
   create_table = "CREATE TABLE IF NOT EXISTS %s (stock_symbol text, trade_time timestamp, trade_price float, PRIMARY KEY(stock_symbol, trade_time))" %s (args.topic)
   sesson.execute(create_table) 
   consumer = KafkaConsumer(args.topic, bootstrap_servers = [args.kafka_url])
   for message in consumer:
        print("topic : %s, message value %s" % (message.topic, message.value))
        store_data(session, message)
