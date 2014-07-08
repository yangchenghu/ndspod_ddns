#!/usr/bin/env python
#-*- coding:utf-8 -*-

import httplib, urllib
import socket
import time
import re,urllib2

strDomain = "subDomain.domain.com"

params = dict(
    login_email="youremail", # replace with your email
    login_password="yourpassword", # replace with your password
    format="json",
    domain_id=1000, # replace with your domain_od, can get it by API Domain.List
    record_id=1000, # replace with your record_id, can get it by API Record.List
    sub_domain="subDomain", # replace with your sub_domain
    record_line="默认"
)

def ddns(ip):
    params.update(dict(value=ip))
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)

    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200

def getip():
    req = urllib2.Request(url = "http://www.net.cn/static/customercare/yourip.asp")
    webObj = urllib2.urlopen(req)
    assert 200 == webObj.code
    reposne =  webObj.read()
    return re.search('\d+\.\d+\.\d+\.\d+', reposne).group(0)

def getIpFormDomain(domain):
    myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
    return myaddr

if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            print "route ip is:%s" % ip
            strDomainIp = getIpFormDomain(strDomain)
            print "domain ip is:%s" % strDomainIp
            if strDomainIp != ip:
                ddns(ip)
        except Exception, e:
            print e
            pass
        time.sleep(600)