#!/bin/bash
set -e 

docker run --rm -i \
-v $(pwd):/demo/ \
-w /demo \
docker.dg-atlas.com:5000/demo-test:1.0 \
./deploy.sh

docker run --rm -i \
-v $(pwd):/demo/ \
-w /demo \
docker.dg-atlas.com:5000/demo-test:1.0 \
python function_test.py

docker run --rm -i \
-v $(pwd):/demo/ \
-w /demo \
docker.dg-atlas.com:5000/demo-test:1.0 \
python pressure.py  >  out.file  2>&1  &

