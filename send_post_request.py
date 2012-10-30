#!/usr/bin/env python
#coding:utf-8
import httplib, urllib
import datetime
import time
def send():
	test_data = {'firstname':'wangyongle'}
	test_data_urlencode = urllib.urlencode(test_data)
	requrl="http://172.16.17.101/oa/main/errorindex"
	headerdata = {"Host":"172.16.17.101"}
	conn = httplib.HTTPConnection("172.16.17.101")
	#headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn.request(method="POST",url=requrl,body=test_data_urlencode,headers=headerdata)
	response = conn.getresponse()
	data = response.read()
	if data:
		return True
	else :
		print 'no data'
		return False
	print data
   	time.sleep(0.1)
	conn.close() 
if __name__ == '__main__':
	send()
