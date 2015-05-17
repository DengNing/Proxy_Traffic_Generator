##dengning
import urllib2
import socket
import thread  
import random,re,time
#import requests
#import multiprocessing
lis = []
#timeout = 2
#socket.setdefaulttimeout(timeout)
for line in open("plist.txt"):
    col = line.split()
    if len(col) >=1:
        a = col[1]
        b = col[2]
        c = a + ':' + b
        lis.append(c)
for line in open("proxylist.txt"):
    col = line.split()
    if len(col) >=1:
        lis.append(c)
num_Error=0
num_Success=0

for ip in open("proxy1.txt"):
    try:
        proxy = ip
        proxy_handler = urllib2.ProxyHandler({'http':'http://'+ip})
        opener=urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        response = urllib2.urlopen('http://www.baidu.com')
        print response.code
        num_Success +=1
        print "%d Sucess" %num_success
    except urllib2.URLError:          
         print "BAD Proxy is %s" % ip
         num_Error += 1
    except urllib2.HTTPError:
         print 'HTTPError! The bad proxy is %s' % ip
         num_Error += 1
    except:
         print "Unknow Errors! The bad proxy is %s" % ip
         num_Error += 1
         print "%d Error" %num_Error 
print "%d num_Success" % num_Seccess
print "%d num_Error"  %num_Error