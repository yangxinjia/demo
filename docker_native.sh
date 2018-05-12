#!/bin/bash
set -e 

docker run --rm -i \
-v /data_1/jenkins/workspace/demo:/demo/ \
-w /demo \
docker.dg-atlas.com:5000/golang:1.9 \
./build_native.sh
