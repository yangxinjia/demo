#!/bin/bash

##########################

declare -a Util_0
declare -a Util_1
declare -a result

total_time=20
interval=1
times_e=1
times=$(($total_time/$(($interval*$times_e))))
sum_0=0
sum_1=0
##########################

while ((i<$times))
do
    j=0
    while((j<$times_e))
    do
   	Util_1=$(top -b -d 1 -n 1 | grep matrix | awk '{print $9}')
   	Util_1[j]=${Util_1%.*}
#   	echo "sum_0:"$sum_0
   	sum_1=$(($sum_1+${Util_1[j]}))
#   	echo "sum_1:"$sum_1
   	j=$(($j+1))
   	sleep $interval
    done
#    res_0=$(python cal.py $point $sum_0)
    res_1=$(python cal.py $times_e $sum_1)
#    echo $res_0"%"
    result[i]=$res_1
#    echo $res_1"%"
    sum_0=0
    sum_1=0
    i=$(($i+1))
done
i=0
file="../logs/demo-cpu.log"
mkdir -p ../logs
touch $file
echo >> $file
date >>$file
echo "CPU used:" >> $file
echo "         1         2         3         4         5         6         7         8" >> $file
while ((i<$times))
do
    result_t=${result[$i]%.*}
    j=0
    result_this=$(($result_t/10))
    while ((j<$result_this))
    do
        echo -e "#\c" >>$file
        j=$(($j+1))
    done
    echo " "$result_t>> $file
    i=$(($i+1))
done
echo

python draw.py cpu "${result[@]}"
