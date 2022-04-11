#!/bin/bash

docker build . -t hw1_docker:1.0
docker run hw1_docker:1.0
