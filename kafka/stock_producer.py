#! /usr/bin/python 

from googlefinance import getQuotes
from kafka import KafkaProducer
import json
import schedule 
import time

# get stock data structure stock_json from third party module - googlefinance 
def send_stock_info(producer, symbol):
    stock_json = getQuotes(symbol)
    stock_symbol = stock_json[0]['StockSymbol']
    stock_lastTradeTime = stock_json[0]['LastTradeTime']
    stock_lastTradePrice = float(stock_json[0]['LastTradePrice'])
    print(stock_symbol, stock_lastTradeTime, stock_lastTradePrice)
    payload = ('{"StockSymbol : %s, "LastTradeTime" : %s, "LastTradePrice" : %.2f}' % (stock_symbol, stock_lastTradeTime, stock_lastTradePrice)).encode("utf-8")
    producer.send("stock", payload)

if __name__ == "__main__":
    print("haha1")
    producer = KafkaProducer()
    schedule.every().second.do(send_stock_info, producer, 'FB')
    print("haha2")
    while True:
        schedule.run_pending()
        time.sleep(4)

