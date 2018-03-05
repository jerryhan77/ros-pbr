#!/bin/sh
FILE=ip_apnic
rm -f $FILE 
wget http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest -O $FILE
grep 'apnic|CN|ipv4|' $FILE | cut -f 4,5 -d'|'|sed -e 's/|/ /g' | while read ip cnt
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
       	echo $ip/$mask>> cn.net
	NETNAME=`whois $ip@whois.apnic.net | sed -e '/./{H;$!d;}' -e 'x;/netnum/!d' |grep ^netname | sed -e 's/.*:      \(.*\)/\1/g' | sed -e 's/-.*//g'`
	case $NETNAME in 
	CNC)
		echo $ip/$mask >> CNCGROUP
	;;
	CHINANET|CNCGROUP)
		echo $ip/$mask >> $NETNAME
	;;
	CHINANET|CNCGROUP)
		echo $ip/$mask >> $NETNAME
	;;
	CHINATELECOM)
		echo $ip/$mask >> CHINANET
	;;
	*)
		echo $ip/$mask >> OTHER
	;;
	esac
done

