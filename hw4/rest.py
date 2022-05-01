from flask import Flask, request, jsonify
from read_from_cassandra import CassandraClient
import json


app = Flask(__name__)
host = 'localhost'
port = 9042
keyspace = 'hw4_hnatenko'

client = CassandraClient(host, port, keyspace)
client.connect()
app.run(host=host, port=8080)


@app.get("/reviews_with_product_id/<product_id>")
def get_reviews_for_product_id(product_id):
    # Return all reviews for specified product_id
    return json.dumps(client.select1(product_id), indent=4, sort_keys=True, default=str)


@app.get("/reviews_with_product_id/<product_id>/<star_rating>")
def get_reviews_for_product_id_by_rating(product_id, star_rating):
    # Return all reviews for specified product_id with given star_rating
    return json.dumps(client.select2(product_id, star_rating), indent=4, sort_keys=True, default=str)


@app.get("/reviews_with_customer_id/<customer_id>")
def get_reviews_for_product_rating(customer_id):
    # Return all reviews for specified customer_id
    return json.dumps(client.select3(customer_id), indent=4, sort_keys=True, default=str)


@app.get("/top_products/<n>/<date>1/<date2>")
def get_top_products_by_num_reviews_period(n, date1, date2):
    # Return N most reviewed items (by # of reviews) for a given period of time
    return json.dumps(client.select4(n, date1, date2), indent=4, sort_keys=True, default=str)


@app.get("/top_customers/<n>/<date>1/<date2>")
def get_top_customers_by_num_reviews_period(n, date1, date2):
    # Return N most productive customers (by # of reviews written for verified purchases) for a given period
    return json.dumps(client.select5(n, date1, date2), indent=4, sort_keys=True, default=str)


@app.get("/top_haters/<n>/<date>1/<date2>")
def get_top_customers_by_num_reviews_period(n, date1, date2):
    # Return N most productive “haters” (by # of 1- or 2-star reviews) for a given period
    return json.dumps(client.select6(n, date1, date2), indent=4, sort_keys=True, default=str)


@app.get("/top_haters/<n>/<date>1/<date2>")
def get_top_customers_by_num_reviews_period(n, date1, date2):
    # Return N most productive “backers” (by # of 4- or 5-star reviews) for a given period
    return json.dumps(client.select7(n, date1, date2), indent=4, sort_keys=True, default=str)
