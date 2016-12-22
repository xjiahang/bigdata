#! /usr/bin/python 

from googlefinance import getQuotes
from kafka import KafkaProducer
import json
import schedule 
import time
import argparse

# get stock data structure stock_json from third party module - googlefinance 
def send_stock_info(producer, topic, symbol):
    stock_json = getQuotes(symbol)
    stock_symbol = stock_json[0]['StockSymbol']
    stock_lastTradeTime = stock_json[0]['LastTradeTime']
    stock_lastTradePrice = float(stock_json[0]['LastTradePrice'])
    print(stock_symbol, stock_lastTradeTime, stock_lastTradePrice)
    payload = ('{"StockSymbol : %s, "LastTradeTime" : %s, "LastTradePrice" : %.2f}' % (stock_symbol, stock_lastTradeTime, stock_lastTradePrice)).encode("utf-8")
    producer.send(topic, payload)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('kafka_url', help = 'url of kafka broker')
    parser.add_argument('topic', help = 'kakfa topic that the message published to')
    parser.add_argument('stock_symbol', help = 'stock symbol users want to view')
    args = parser.parse_args()


    producer = KafkaProducer(bootstrap_servers = [args.kafka_url])
    schedule.every().second.do(send_stock_info, producer, args.topic, args.stock_symbol)
    while True:
        schedule.run_pending()
        time.sleep(4)

