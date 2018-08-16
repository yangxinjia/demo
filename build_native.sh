#!/bin/bash
set -e

name=$(basename `pwd`)-$(cat VERSION)
rm -rf push_${name}.sh
cmd="scp "
mkdir -p doc

project=$(basename `pwd`)-$(cat VERSION)
echo "Build native ${project} start"
mkdir -p release/native/${project}

go build -o demo .
cp demo release/native/${project}
cp README.md release/native/${project}
cp VERSION release/native/${project}
cp run_native.sh release/native/${project}
cp -r conf release/native/${project}
cd release/native
tar -czvf ${project}.tar.gz ${project}
cmd=${cmd}${project}".tar.gz "
cd ../..
echo "Build native ${project} finished"

cmd=${cmd}"root@file.dg-atlas.com:/data_0/ftp/private/release/mserver/native/"
rm -rf release/native/push_${name}.sh
echo "${cmd}"  | cat >> release/native/push_${name}.sh
chmod +x release/native/push_${name}.sh
