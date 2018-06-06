#!/bin/bash
set -e 

docker run --rm -i \
-v $(pwd):/go/src/demo/ \
-v $(pwd)/../github.com/:/go/src/github.com/ \
-w /go/src/demo \
docker.dg-atlas.com:5000/golang:1.9 \
./build_native.sh
