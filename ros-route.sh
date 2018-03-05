#!/bin/sh

echo ":foreach i in=[/ip route rule find ] do=[/ip route rule remove \$i]"
echo "/ip route rule"

nets=`cat ipip/CNCGROUP`

for net in $nets ; do
  echo "add dst-address=$net action=lookup table=CNC"
done

nets=`cat ipip/CHINANET`
for net in $nets ; do
  echo "add dst-address=$net action=lookup table=CT"
done

nets=`cat ipip/CMNET`
for net in $nets ; do
  echo "add dst-address=$net action=lookup table=CMCC"
done
