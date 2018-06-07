#!/bin/bash
set -e 

docker run --rm -i \
-v $(pwd):/go/src/demo/ \
-w /go/src/demo \
docker.dg-atlas.com:5000/demo-compile:1.0 \
./build_native.sh
