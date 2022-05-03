from cassandra.query import dict_factory


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        from cassandra.cluster import Cluster
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)
        self.session.row_factory = dict_factory
        # print(hi)

    def execute(self, query):
        self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def select1(self, product_id):
        """
        Return all reviews for specified product_id
        :param product_id: str
        :return: dict
        """
        query = f"SELECT review_id, review_headline,review_body,star_rating FROM products WHERE product_id = '{product_id}';"
        return list(self.session.execute(query))

    def select2(self, product_id, star_rating):
        """
         Return all reviews for specified product_id with given star_rating
        :param product_id: str
        :param star_rating: int
        :return: dict
        """
        query = f"SELECT review_id, review_headline,review_body, star_rating FROM products WHERE product_id = '{product_id}' AND " \
                f"star_rating = {star_rating};"
        return list(self.session.execute(query))

    def select3(self, customer_id):
        """
        Return all reviews for specified customer_id
        :param customer_id: int
        :return: dict
        """
        query = f"SELECT review_id, review_headline,review_body FROM reviews WHERE customer_id = '{customer_id}';"
        return list(self.session.execute(query))

    def select4(self, N, date1, date2):
        """
        Return N most reviewed items (by # of reviews) for a given period of time
        :param N: int
        :param date1: str
        :param date2: str
        :return: dict
        """
        query = f"SELECT product_id, COUNT(*) from products WHERE (review_date >= '{date1}') AND " \
                f"(review_date < '{date2}') GROUP BY product_id ALLOW FILTERING; "
        return list(sorted(self.session.execute(query), key=lambda d: d['count'], reverse=True))[:N]

    def select5(self, N, date1, date2):
        """
        Return N most productive customers (by # of reviews written for verified purchases) for a given period
        :param N: int
        :param date1: str
        :param date2: str
        :return: dict
        """
        query = f"SELECT customer_id, COUNT(*) from reviews WHERE verified_purchase = 'Y' AND (review_date >= '{date1}') AND (" \
                f"review_date < '{date2}') GROUP BY customer_id ALLOW FILTERING; "
        return list(sorted(self.session.execute(query), key=lambda d: d['count'], reverse=True))[:N]

    def select6(self, N, date1, date2):
        """
        Return N most productive “haters” (by # of 1- or 2-star reviews) for a given period
        :param N: int
        :param date1: str
        :param date2: str
        :return: dict
        """
        query = f"SELECT customer_id, COUNT(*) from reviews WHERE (star_rating < 3) AND (review_date >= '{date1}') AND (" \
                f"review_date < '{date2}') GROUP BY customer_id ALLOW FILTERING; "
        return list(sorted(self.session.execute(query), key=lambda d: d['count'], reverse=True))[:N]

    def select7(self, N, date1, date2):
        """
        Return N most productive “backers” (by # of 4- or 5-star reviews) for a given period
        :param N: int
        :param date1: str
        :param date2: str
        :return: dict
        """
        query = f"SELECT customer_id, COUNT(*) from reviews WHERE (star_rating >= 3) AND (review_date >= '{date1}') " \
                f"AND (review_date < '{date2}') GROUP BY customer_id ALLOW FILTERING;"
        return list(sorted(self.session.execute(query), key=lambda d: d['count'], reverse=True))[:N]


def cassandra_connect(host='localhost', port=9042, keyspace='hw4_hnatenko'):
    client = CassandraClient(host, port, keyspace)
    client.connect()
    d1 = client.select1('0385730586')
    d2 = client.select2('0385730586', 5)
    d3 = client.select3('12257412')
    d4 = client.select4(10, '2005-10-14', '2016-10-14')
    d5 = client.select5(10, '2005-10-14', '2015-10-14')
    print(d4)
    d6 = client.select6(10, '2005-08-31', '2015-08-31')
    d7 = client.select7(10, '2005-08-31', '2015-08-31')
    client.close()


if __name__ == '__main__':
    cassandra_connect()
