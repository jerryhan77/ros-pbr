#!/usr/bin/python

import sys
from collections import defaultdict
route_map=defaultdict(set)
try:
    input_file=open(sys.argv[1],'r')
except:
    input_file=sys.stdin
iplist=set()
ln=0
for line in input_file:
    ln+=1
    try:
        ip,mask=line.split('/')
        mask=32-int(mask)
        ip=reduce(lambda a,b:(a<<8)+b,[int(i) for i in ip.split('.')])>>mask
    except:
        print >>sys.stderr,'%d invaild data' % ln
        continue
    iplist.add((mask,ip))
for mask,ip in sorted(iplist,reverse=True):
    for i in sorted((k for k in route_map.iterkeys() if k>=mask)):
        ip_set=route_map[i]
        if i==mask:
            if ip in ip_set:
                break
            if ip^1 in ip_set:
                ip_set.remove(ip^1)
                ip=ip/2
                mask+=1
        else:
            if ip>>i-mask in ip_set:
                break
    else:
        route_map[mask].add(ip)
for mask in route_map.iterkeys():
    for ip in route_map[mask]:
        ip=ip<<mask
        first = int((ip >> 24) & 255)
        second = int((ip >> 16) & 255)
        third = int((ip >> 8) & 255)
        fourth = int(ip & 255)
        print '%d.%d.%d.%d/%d' % (first, second, third, fourth,32-mask)
