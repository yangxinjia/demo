#:/bin/bash

##########################

declare -a Util_0
declare -a Util_1
declare -a result

total_time=120
interval=1
times_e=3
times=$(($total_time/$(($interval*$times_e))))
sum_0=0
sum_1=0
##########################

while ((i<$times))
do
    j=0
    while((j<$times_e))
    do
   	Util_1=$(nvidia-smi | grep Default | awk NR==2 |awk '{print $9}' |sed 's/MiB//')
   	Util_1[j]=${Util_1}
   	sum_1=$(($sum_1+${Util_1[j]}))
#   	echo "sum_1:"$sum_1
   	j=$(($j+1))
   	sleep $interval
    done
    res_1=$(python cal.py $times_e $sum_1)
    result[i]=$res_1
#    echo $res_1"%"
    sum_0=0
    sum_1=0
    i=$(($i+1))
done
i=0
file="../logs/demo-g_mem.log"
mkdir -p ../logs
touch $file
echo >> $file
date >> $file
echo "GPU used:" >>$file
echo "         10        20        30        40        50        60        70        80        90        100">>$file
while ((i<$times))
do
    result_t=${result[$i]%.*}
    result_this=$(($result_t/100))
    j=0
    while ((j<$result_this))
    do
        echo -e "#\c"  >>$file
        j=$(($j+1))
    done
    echo " "$result_t>> $file
    i=$(($i+1))
done
echo

