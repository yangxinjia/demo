#!/bin/bash

docker rm -f demo

docker run -i -t -d \
--net="host" --privileged --restart=always --name=demo \
-v $(pwd)/conf/:/demo/conf/ \
docker.dg-atlas.com:5000/demo:$(cat VERSION) \
./demo
