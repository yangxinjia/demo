#!/bin/bash
function check(){
    sed -i 's/$(pwd)/\/data_1\/jenkins\/workspace\/test_t-UFA55RUYY7VIA2BSHBFS4EBOCEL3NMA6JBVBQZDXJ7ZJ7XYHPV2Q/' docker_image.sh
    exit
}
function compile(){
    ./docker_image.sh
    exit
}
function test(){
    nosetests demo_test.py --with-xunit  demo_test.xml
    exit
}
function run(){
    cd release/images/demo-$(cat VERSION)/
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
