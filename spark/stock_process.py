
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("spark_url", help = "spark_url for master parameter")
    parser.add_argument("app_name", help = "application name")
    args = parser.parse_args()

    spark_url = args.spark_url
    app_name = args.app_name

    sc = SparkContext(spark_url, app_name)
    ssc = StreamingContext(sc, 4)


