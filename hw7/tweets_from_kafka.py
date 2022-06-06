from json import loads
from kafka import KafkaConsumer
from csv import writer

consumer = KafkaConsumer('tweets',
                         bootstrap_servers=['kafka-server:9092'],
                         api_version=(2,0,2),
                         value_deserializer=lambda x:
                         loads(x.decode('ascii')))


def main():
    curr_date = ''
    curr_date_messages = []
    for message in consumer:
        message = message.value
        # print(curr_date_messages)
        # print(message['created_at'])
        if message['author_id'] == 'the_end' or message['created_at'] != curr_date:
            # print('curr_date:', curr_date)
            if message['author_id'] == 'end':
                curr_date = message['created_at']
            filename = f'tweets_{curr_date}.csv'
            with open(filename, 'w+') as f:
                write = writer(f)
                write.writerow(['author_id', 'created_at', 'text'])
                write.writerows(curr_date_messages)
                print('wrote all')
                curr_date_messages = []
            if message['author_id'] == 'the_end':
                exit(0)
            curr_date = message['created_at']

        curr_date_messages.append([message['author_id'], message['created_at'], message['text']])


if __name__ == '__main__':
    # print('reading tweets...')
    main()

