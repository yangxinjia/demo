#!/bin/bash
function compile(){
    ./docker_image.sh
    exit
}
function test(){
    nosetests demo_test.py --with-xunit  demo_test.xml
    exit
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
    echo "<ci.sh usage : build / end>"
    exit
fi
if [ "$1" == "compile" ];then
    build
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
