from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import date, timedelta
import csv
import random

producer = KafkaProducer(bootstrap_servers=['kafka-server:9092'],
                         api_version=(2,0,2),
                         value_serializer=lambda x:
                         dumps(x).encode('ascii'))


def get_transaction_date():
    end_date = date.today()
    random_date = end_date - timedelta(days=random.randint(20,30))
    return str(random_date)


def main():
    with open('./PS_20174392719_1491204439457_log.csv', 'r') as f:
        # print('opened file')
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            # step,type,amount,nameOrig,oldbalanceOrg,newbalanceOrig,nameDest,oldbalanceDest,newbalanceDest,isFraud,isFlaggedFraud
            # 1,2,3,4,6,-2

            row = [row[1],row[2],row[3],row[6],row[-2]]
            row.append(get_transaction_date())
            producer.send('kafka-topic', row)
            sleep(0.1)
            print('sent')

        producer.flush()


if __name__ == '__main__':
    main()
