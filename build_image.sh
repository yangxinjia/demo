#!/bin/bash
set -e
project=$(basename `pwd`)
version=$(cat VERSION)
echo "Build image ${project} start"
go build -o demo .
docker build -t docker.dg-atlas.com:5000/${project}:${version} .
mkdir -p release/images/${project}-${version}
cd release/images/${project}-${version}
docker save -o ${project}-${version}.img docker.dg-atlas.com:5000/${project}:${version}
cp ../../../VERSION .
cp ../../../README.md .
cp ../../../run_image.sh .
cp ../../../conf . -r
cd ..
tar -czvf ${project}-${version}.tar.gz ${project}-${version}
echo "Build image ${project} finished"
