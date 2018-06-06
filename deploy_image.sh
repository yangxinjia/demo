#!/bin/bash
version=$(cat VERSION)
cp $(pwd)/release/images/demo-$version.tar.gz /root/work/
cd /root/work/
tar -zxvf demo-$version.tar.gz
cd demo-$version
./run_image.sh
