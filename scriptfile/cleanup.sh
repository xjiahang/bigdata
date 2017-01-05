#! /bin/bash 

../kafka_2.11-0.10.0.1/bin/kafka-topics.sh --zookeeper localhost --delete --topic stock1
../kafka_2.11-0.10.0.1/bin/kafka-topics.sh --zookeeper localhost --delete --topic stock2
