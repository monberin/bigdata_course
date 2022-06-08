### to run:
```
sh ./to-kafka/run-kafka-cluster.sh 
sh ./cassandra/run-cassandra-cluster.sh
```
separate terminals:
```
sh ./kafka-cassandra/read_tweets.sh
```
```
sh ./to-kafka/run_transactions.sh
```
```
sh ./kafka-cassandra/rest.sh
```
### checking how many entries were written in the console
![Screenshot from 2022-06-08 12-45-07](https://user-images.githubusercontent.com/56642774/172615709-ef0f1ace-16d1-4bb8-87f7-7f8d598c4a33.png)
![Screenshot from 2022-06-08 12-51-25](https://user-images.githubusercontent.com/56642774/172615718-c77e18da-5ee4-4d3b-ae96-652bb50310e3.png)
### different queries and the results
![Screenshot from 2022-06-08 12-47-57](https://user-images.githubusercontent.com/56642774/172615730-d4ae3f72-a331-4461-872e-0dd5c1b41305.png)
![Screenshot from 2022-06-08 12-54-02](https://user-images.githubusercontent.com/56642774/172615735-e749f949-f608-47ce-97ae-26b896cc499b.png)
![Screenshot from 2022-06-08 12-55-13](https://user-images.githubusercontent.com/56642774/172615745-efa35fb5-b678-40f9-9290-30a5959a39a5.png)
![Screenshot from 2022-06-08 12-57-32](https://user-images.githubusercontent.com/56642774/172615751-0e7135b9-af79-4d9b-bc0e-ce63b9658923.png)
![Screenshot from 2022-06-08 12-57-59](https://user-images.githubusercontent.com/56642774/172615757-eb3c71dc-6d03-43dd-9f85-15c23703ecc2.png)
