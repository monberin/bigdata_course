CREATE KEYSPACE hw8 WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE hw8;
DROP TABLE IF EXISTS uid_fraud;
CREATE TABLE IF NOT EXISTS uid_fraud (
    uid text,
    isFraud int,
    transaction_type text,
    amount float,
    transaction_date date,
    PRIMARY KEY (uid, isFraud));

DROP TABLE IF EXISTS uid_big;
CREATE TABLE IF NOT EXISTS uid_big (
    uid text,
    isFraud int,
    transaction_type text,
    amount float,
    transaction_date date,
    PRIMARY KEY (uid, amount));

DROP TABLE IF EXISTS reciever_uid;
CREATE TABLE IF NOT EXISTS reciever_uid (
    reciever_uid text,
    isFraud int,
    transaction_type text,
    amount float,
    transaction_date date,
    PRIMARY KEY (reciever_uid, transaction_date));


-- docker exec -it node1 cqlsh -e