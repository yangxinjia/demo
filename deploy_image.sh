#!/usr/bin/expect              
version=$(cat VERSION)
set timeout 3
spawn scp ./release/images/demo-$version.tar.gz root@172.24.156.85:~/work/
expect "password"
send "L70aSp12\r"
interact

set timeout 3
spawn ssh root@172.24.156.85 "cd work; tar -zxvf demo-$version.tar.gz; cd demo-$version; ./run_image.sh"
expect "password"
send "L70aSp12\r"
interact
