### running docker-compose
```
docker-compose up -d  
```
![Screenshot from 2022-06-08 15-04-38](https://user-images.githubusercontent.com/56642774/172618849-76541046-22b8-4602-9e97-227f055da9d2.png)
```
docker run --rm -it --network spark-network --name spark-submit -v <your path>:/opt/app bitnami/spark:3 /bin/bash

```
![Screenshot from 2022-06-08 14-42-57](https://user-images.githubusercontent.com/56642774/172618835-a11512c5-32e2-4cb2-a193-b33d33477855.png)
```
cd opt/app
spark-submit --master local[*] --deploy-mode client SimpleProgram.py
```
### results
![Screenshot from 2022-06-08 14-45-21](https://user-images.githubusercontent.com/56642774/172618840-5ab75e84-c6de-4a80-ae2b-94569847d02d.png)
### to shutdown docker-compose
```
docker-compose down 
```
