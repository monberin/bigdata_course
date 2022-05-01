#!/bin/bash
QUERY="
CREATE KEYSPACE hw4_hnatenko WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE hw4_hnatenko;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS reviews;
CREATE TABLE IF NOT EXISTS products (
    product_id text,
    star_rating int,
    review_id text,
    review_headline text,
    review_body text,
    review_date date,
    PRIMARY KEY (product_id, star_rating));

CREATE TABLE IF NOT EXISTS reviews (
    review_id text,
    customer_id text,
    product_id text,
    verified_purchase text,
    star_rating int,
    review_headline text,
    review_body text,
    review_date date,
    PRIMARY KEY (customer_id, review_id));
    DESCRIBE TABLES"

docker exec -it node1 cqlsh -e "${QUERY}"