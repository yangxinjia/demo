#!/bin/bash

set -e

docker run --rm -i \
-v /data_1/jenkins/workspace/demo:/go/src/github.com/yangxinjia/demo \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /var/lib/docker:/var/lib/docker \
-v /usr/bin/docker:/usr/bin/docker \
-v /usr/lib/x86_64-linux-gnu/libltdl.so.7:/usr/lib/x86_64-linux-gnu/libltdl.so.7 \
-w /go/src/github.com/yangxinjia/demo \
docker.dg-atlas.com:5000/golang:1.9 \
./build_image.sh
