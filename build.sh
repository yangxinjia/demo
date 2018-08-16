#!/bin/bash
function check(){
    exit 0
}
function compile(){
    ./docker_image.sh
    exit
}
function test(){
    mkdir -p report
    nosetests demo_test.py --with-xunit --xunit-file=./report/result.xml
    exit 0
}
function run(){
    ./run_image.sh
    exit
}
function end(){
    echo "end"
    exit
}
if [ $# != 1 ];then
    echo "<build.sh usage : check / compile / test / run / end>"
    exit
fi
if [ $1 == "check" ];then
    check
fi
if [ "$1" == "compile" ];then
    compile
fi
if [ "$1" == "run" ];then
    run
fi
if [ "$1" == "test" ];then
    test
fi
if [ "$1" == "end" ];then
    end
fi
echo "not support usage <$1>"
