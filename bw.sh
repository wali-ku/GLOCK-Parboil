insmod /home/nvidia/ssd/gits/devel/BWLOCK-GPU/kernel_module/exe/bwlockmod.ko
echo 1634 > /sys/kernel/debug/bwlock/corun_threshold_events
sleep 2

bandwidth -c 4 -t 1000 -m 16384 -i 1000000 &
bandwidth -c 5 -t 1000 -m 16 -i 1000000000 &

chrt -f 1 bandwidth -c 4 -t 1000 -m 768 -i 200000 &
chrt -f 1 trace-cmd record -e 'sched_wakeup*' -e 'sched_switch' bandwidth -c 5 -t 1000 -m 768 -i 200000 &
pid=$!
sleep 2

chrt -f 3 bandwidth -c 0 -t 1000 -m 768 -i 200000 &
chrt -f 3 bandwidth -c 1 -t 1000 -m 768 -i 200000

wait ${pid}
rmmod bwlockmod
sleep 5
killall bandwidth
