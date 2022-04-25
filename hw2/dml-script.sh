#!/bin/bash
QUERY="
  USE hw2_hnatenko;
  INSERT INTO favorite_songs( id, author, song_name, release_year) VALUES (1, 'Placebo', 'Beautiful James', 2021);
  INSERT INTO favorite_songs( id, author, song_name, release_year) VALUES (2, 'Deftones', 'Be Quiet and Drive (Far Away)', 1997);

  INSERT INTO favorite_movies ( id, name, producer, release_year) VALUES (1, 'Amelie', 'Jean-Pierre Jeunet', 2001);
  INSERT INTO favorite_movies ( id, name, producer, release_year) VALUES (2, 'Castle in the Sky', 'Hayao Miyazaki', 1986);
  
  SELECT * FROM favorite_songs;
  SELECT * FROM favorite_movies;
  "

docker exec -it node1 cqlsh -e "${QUERY}"