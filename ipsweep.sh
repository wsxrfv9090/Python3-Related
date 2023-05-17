#!/bin/bash

if [ "$1" == "" ]
then
echo "You forgot an ip address!"
echo "Syntax: ./ipsweep.sh 192.168.x.y"

else
for ip1 in `seq 1 254`; do
for ip2 in `seq 1 254`; do
ping -c 1 $1.$ip1.$ip2 | grep "64 bytes" | cut -f 4 -d " " | tr -d ":" &
done
done
fi
