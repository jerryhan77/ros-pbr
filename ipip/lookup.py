#!/usr/bin/python

# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
import time
import urllib2
con = None 
count=1000
delay=1
reload(sys)
sys.setdefaultencoding('utf-8')
try:
    con = mdb.connect('localhost', 'root', '', 'ipip', charset='utf8');
    cur = con.cursor()
    cur.execute("select Network from NETWORKS where FetchTime is null")
    rows = cur.fetchmany(count)
    for row in rows:
        network=row[0]
        ip = network.split('/')[0]
        url = "http://freeapi.ipip.net/" + ip
        isp='';
        try: 
            response = urllib2.urlopen(url)
            html = response.read().replace('[','').replace(']','').replace('"','')
            result = html.split(',')
            if len(result) >= 5:
                isp = result[4]
            cur.execute("UPDATE NETWORKS SET ISP = %s, FetchTime = now() WHERE Network = %s", (isp, network))
            print url,isp
        except urllib2.HTTPError, e:
            print url, 'ERROR', e.code
            #print e.read()
	time.sleep(delay)

except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
finally:    
    if con:    
        con.close()

