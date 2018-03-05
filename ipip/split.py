#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
con = None 
count=0
reload(sys)
sys.setdefaultencoding('utf-8')
try:
# CHINANET/CNCGROUP/CMNET/CN
    chinanet= open('CHINANET','w')
    cncgroup= open('CNCGROUP','w')
    cmnet= open('CMNET','w')
    cn= open('CN','w')
       
    con = mdb.connect('localhost', 'root', '', 'ipip', charset='utf8');
    cur = con.cursor()
    cur.execute("select Network,ISP from NETWORKS")
    rows = cur.fetchall()
    for row in rows:
        network=row[0]
        isp = row[1]
        print count,network,isp
        count += 1
        if isp.find('移动')>=0:
            cmnet.write("%s\n" % network)
        elif isp.find('电信') >=0: 
            chinanet.write("%s\n" % network)
        elif isp.find('CHINATELECOM')>=0:
            chinanet.write("%s\n" % network)
        elif isp.find('联通')>=0:
            cncgroup.write("%s\n" % network)
        elif isp.find('铁通')>=0:
            cmnet.write("%s\n" % network)
        else:   
            cn.write("%s\n" % network)
    
    cur.close()    
    
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
# CHINANET/CNCGROUP/CMNET/CN
