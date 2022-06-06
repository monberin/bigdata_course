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
    return datetime.today().strftime('%d_%m_%Y_%H_%M')


def main():
    with open('twcs.csv', 'r') as f:
        # print('opened file')
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            row[3] = get_curr_time()
            tweet = {'author_id': row[1], 'created_at': row[3], 'text': row[4]}
            producer.send('tweets', tweet)
            sleep(0.1)
        producer.send('tweets', {'author_id':'the_end', 'created_at': row[3], 'text': ''})
        producer.flush()


if __name__ == '__main__':
    main()
