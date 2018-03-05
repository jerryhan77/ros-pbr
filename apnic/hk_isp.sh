#!/bin/sh
FILE=ip_apnic
rm -f $FILE 
rm -f hk.net
wget http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest -O $FILE
grep 'apnic|HK|ipv4|' $FILE | cut -f 4,5 -d'|'|sed -e 's/|/ /g' | while read ip cnt
do
	echo $ip:$cnt
        mask=$(cat << EOF | bc | tail -1
pow=32;
define log2(x) {
if (x<=1) return (pow);
pow--;
return(log2(x/2));
}
log2($cnt)
EOF)
       	echo $ip/$mask>> hk.net
done

