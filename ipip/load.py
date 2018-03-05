#!/usr/bin/python

# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
con = None 
try:
    con = mdb.connect('localhost', 'root', '', 'ipip');
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS \
        NETWORKS (Network VARCHAR(20) PRIMARY KEY, ISP VARCHAR(20), FetchTime DateTime, Last TIMESTAMP) COLLATE utf8_unicode_ci")
    cur.execute("TRUNCATE TABLE NETWORKS")
    f = open('china_ip_list.txt', 'r')
    for line in f:
        line = line.replace('\n','')
        #print line
        cur.execute("INSERT INTO NETWORKS(Network) VALUES('" + line + "') ON DUPLICATE KEY UPDATE Last = now()")
    f.close()
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
finally:    
    if con:    
        con.close()

