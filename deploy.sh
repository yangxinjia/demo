#!/usr/bin/expect
spawn scp ./release/images/demo-0.0.1.tar.gz root@172.24.156.85:~/work/
expect "password:"
send "L70aSp12\r"
expect eof
spawn ssh root@172.24.156.85 "cd work; tar -zxvf demo-0.0.1.tar.gz; cd demo-0.0.1; ./run_image.sh"
expect "password:"
send "L70aSp12\r"
expect eof
