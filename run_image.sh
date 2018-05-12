#!/bin/bash

docker rm -f demo

docker run -i -t \
--net="host" --privileged --restart=always --name=demo \
docker.dg-atlas.com:5000/demo:$(cat VERSION) \
./demo
