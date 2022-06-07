from json import loads
from kafka import KafkaConsumer


consumer = KafkaConsumer('kafka-topic',
                         bootstrap_servers=['kafka-server:9092'],
                         api_version=(2,0,2),
                         value_deserializer=lambda x:
                         loads(x.decode('ascii')))

class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None
        self.row=0

    def connect(self):
        from cassandra.cluster import Cluster
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)

    # def execute(self, query):
    #     self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def select1(self, uid):
        """
        Return all transactions for uid that were fraudulent
        :param uid: str
        :return: dict
        """
        query = f"SELECT * from uid_fraud WHERE uid = '{uid}' AND isFraud = 1;"
        return list(self.session.execute(query))

    def select2(self, uid):
        """
        Return 3 biggest transactions for uid
        :param uid: str
        :return: dict
        """
        query = f"SELECT * from uid_big WHERE uid = '{uid}';"
        return list(sorted(self.session.execute(query), reverse=True))[:3]

    def select3(self, uid, date1, date2):
        """
        Return sum of all transactions for a uid for a given period of time
        :param uid: str
        :param date1: str
        :param date2: str
        :return: dict
        """
        query = f"SELECT SUM(amount) from reciever_uid WHERE reciever_uid = '{uid}' AND (transaction_date >= '{date1}') AND " \
                f"(transaction_date <= '{date2}'); "
        return list(self.session.execute(query))


    def insert_values(self, table, row):
        # type, amount, uid,reciever_uid,isFraud,transaction_date
        if table == 'uid_fraud' or table == 'uid_big':
            qr = f"INSERT INTO {table} (uid, isFraud, transaction_type, amount, transaction_date) " \
                    f"VALUES ('{row[2]}', {row[4]}, '{row[0]}', {row[1]}, '{row[-1]}')"
            self.session.execute(qr)
        if table == 'reciever_uid':
            qr = f"INSERT INTO {table} (reciever_uid, isFraud, transaction_type, amount, transaction_date) " \
                 f"VALUES ('{row[3]}', {row[4]}, '{row[0]}', {row[1]}, '{row[-1]}')"
            self.session.execute(qr)



def main():
    client = CassandraClient(host='cassandra-server', port=9042, keyspace='hw8')
    client.connect()
    for message in consumer:
        message = message.value
        client.insert_values('uid_fraud', message)
        client.insert_values('uid_big', message)
        client.insert_values('reciever_uid', message)

    client.close()


if __name__ == '__main__':
    main()

