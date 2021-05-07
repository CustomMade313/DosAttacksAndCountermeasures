#!/bin/sh

sleep_counter=$1  #set time in seconds

tcpdump -n icmp >> /dev/null 2> out2 &
pid=$!
sleep $sleep_counter
kill $pid