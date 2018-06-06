#!/bin/bash

set -e

docker run --rm -i -t \
-v $(pwd):/go/src/demo/ \
-v $(pwd)/../github.com/:/go/src/github.com/ \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /var/lib/docker:/var/lib/docker \
-v /usr/bin/docker:/usr/bin/docker \
-v /usr/lib/x86_64-linux-gnu/libltdl.so.7:/usr/lib/x86_64-linux-gnu/libltdl.so.7 \
-w /go/src/demo \
docker.dg-atlas.com:5000/golang:1.9 \
./build_image.sh
