# insmod /home/nvidia/ssd/gits/devel/BWLOCK-GPU/kernel_module/exe/bwlockmod.ko
# echo 1634 > /sys/kernel/debug/bwlock/corun_threshold_events
# sleep 2

bandwidth -c 4 -t 1000 -m 16384 -i 1000000 &
bandwidth -c 5 -t 1000 -m 16 -i 1000000000 &

chrt -f 1 bandwidth -c 4 -t 1000 -m 768 -i 200000 &
pid1=$!
chrt -f 1 bandwidth -c 5 -t 1000 -m 768 -i 200000 &
pid2=$!
sleep 2

chrt -f 3 bandwidth -c 0 -t 1000 -m 768 -i 200000 &
pid3=$!
chrt -f 3 bandwidth -c 3 -t 1000 -m 768 -i 200000

wait ${pid1}
wait ${pid2}
wait ${pid3}
# rmmod bwlockmod
sleep 5
killall bandwidth
