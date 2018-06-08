#!/bin/bash
set -e 

docker run --rm -i \
-v $(pwd):/demo/ \
-w /demo \
docker.dg-atlas.com:5000/demo-test:1.0 \
./deploy.sh && python function_test.py
