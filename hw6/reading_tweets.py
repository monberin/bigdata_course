from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime
import csv

producer = KafkaProducer(bootstrap_servers=['kafka-server:9092'],
                         api_version=(2,0,2),
                         value_serializer=lambda x:
                         dumps(x).encode('ascii'))


def get_curr_time():
    return datetime.today().strftime('%c')


def main():
    with open('sample.csv', 'r') as f:
        # print('opened file')
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            row[3] = get_curr_time()
            tweet = f'{row[3]} sent at {row[4]} by {row[1]}'
            producer.send('topic_tweets', tweet)

        producer.flush()


if __name__ == '__main__':
    main()
