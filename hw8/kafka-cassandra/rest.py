from flask import Flask, request, jsonify
from from_kafka import CassandraClient
import json


app = Flask(__name__)
host = 'cassandra-server'
port = 9042
keyspace = 'hw8'



@app.get("/fraud&uid=<uid>")
def get_fraud_transactions(uid):
    # Return all transactions for uid that were fraudulent
    return json.dumps(client.select1(uid), indent=4, sort_keys=True, default=str)


@app.get("/biggest&uid=<uid>")
def get_biggest_transactions(uid):
    # Return 3 biggest transactions for uid
    return json.dumps(client.select2(uid), indent=4, sort_keys=True, default=str)



@app.get("/sum_trans&uid=<uid>from=<date1>&to=<date2>")
def get_top_products_by_num_reviews_period(uid, date1, date2):
    # Return N most reviewed items (by # of reviews) for a given period of time
    return json.dumps(client.select3(uid, date1, date2), indent=4, sort_keys=True, default=str)





if __name__ == "__main__":
    client = CassandraClient(host='cassandra-server', port=9042, keyspace='hw8')
    client.connect()
    app.run(host='0.0.0.0', port=8080)
