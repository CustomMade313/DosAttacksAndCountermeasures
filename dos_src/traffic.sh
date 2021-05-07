#!/bin/sh

# To find device type on terminal: ip link show
# The one that is UP is the one in use
# Protocol, tcp, udp, etc.
# produces an .out file in the same dir

device=$1
protocol=$2
sleep_counter=$3  #set time in seconds

tcpdump -i $device $protocol >> /dev/null 2> out &
pid=$!
sleep $sleep_counter
kill $pid