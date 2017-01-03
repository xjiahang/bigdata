#! /usr/bin/python
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaProducer

import argparse
import time
import json

producer = None

def process(timeobj, rdd):
    record_count = rdd.count()
    if record_count == 0:
        print "Warning: no record\n"
        return
# - RDD list element
# - (None, u'{"StockSymbol":"AAPL", "LastTradeDateTime":"2016-12-29T12:19:29Z", "LastTradePrice":"116.65"}')    
    price_sum = rdd.map(lambda stock : float(json.loads(stock[1]).get("LastTradePrice"))).reduce(lambda a, b: a + b)
#   print record_count
#   print price_sum
    
    average = price_sum / record_count
    current_time = time.time()
    payload = json.dumps({"timestamp": time.time() , "average_price": average})
    producer.send("redisconsume1", value = payload)
    print payload

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("spark_url", help = "spark_url for master parameter")
    parser.add_argument("app_name", help = "application name")
    parser.add_argument("topic", help = "topic")
    parser.add_argument("kafka_broker", help = "kafka_broker url")

    args = parser.parse_args()
    spark_url = args.spark_url
    app_name = args.app_name
    topic = args.topic
    brokers = args.kafka_broker

    sc = SparkContext("local[2]", app_name)
    ssc = StreamingContext(sc, 4)
    dstream = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
    dstream.foreachRDD(process)
    producer = KafkaProducer()

    ssc.start()
    ssc.awaitTermination()
