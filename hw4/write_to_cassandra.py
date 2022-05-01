import pandas as pd


def form_table():
    df1 = pd.read_csv('amazon_reviews.tsv', sep='\t', nrows=1000)
    df1['review_headline'] = df1['review_headline'].str.replace("'", '"')
    df1['review_body'] = df1['review_body'].str.replace("'", '"')
    prods = df1[['product_id', 'star_rating', 'review_id', 'review_headline', 'review_body', 'review_date']]
    reviews = df1[['review_id', 'customer_id', 'product_id', 'verified_purchase', 'star_rating', 'review_headline',
                   'review_body', 'review_date']]

    return prods, reviews


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


    def insert_products(self, df):
        for index, item in df.iterrows():
            qr = f"INSERT INTO products (product_id, star_rating, review_id, review_headline, review_body," \
                 f" review_date) VALUES ('{item['product_id']}', {round(item['star_rating'])}, '{item['review_id']}'," \
                 f"'{item['review_headline']}','{item['review_body']}', '{item['review_date']}')"
            self.session.execute(qr)

    def insert_reviews(self, df):
        for index, item in df.iterrows():
            qr = f"INSERT INTO reviews (review_id, customer_id, product_id, verified_purchase, star_rating, " \
                 f"review_headline, review_body, review_date) VALUES ('{item['review_id']}', '{item['customer_id']}', " \
                 f"'{item['product_id']}', '{item['verified_purchase']}', {round(item['star_rating'])}, " \
                 f"'{item['review_headline']}', '{item['review_body']}', '{item['review_date']}')"
            self.session.execute(qr)


def cassandra_connect(host='localhost', port=9042, keyspace='hw4_hnatenko'):
    prods, reviews = form_table()

    client = CassandraClient(host, port, keyspace)
    client.connect()
    client.insert_products(prods)
    client.insert_reviews(reviews)
    client.close()


if __name__ == '__main__':
    form_table()
    cassandra_connect()
