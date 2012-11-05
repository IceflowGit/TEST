#!/usr/bin/env python
#coding:utf-8
import httplib, urllib
import datetime
import time
import sys
'''
函数名：send
作用：给OA发送post请求
'''
def send():
	test_data = {'name':'zhangqiang',
			'password':'iceflow',
			'system':'1'}
	test_data_urlencode = urllib.urlencode(test_data)#对数据进行编码
	requrl="http://172.16.17.101/oa/main/login"#连接地址
	conn = httplib.HTTPConnection("172.16.17.101")#连接主机
	headerdata = {"Content-type": "application/x-www-form-urlencoded",
			 "Accept": "text/plain",
			"Host":"172.16.17.101"}#post文件头内容
	conn.request(method="POST",url=requrl,body=test_data_urlencode,headers=headerdata)#发送请求
	response = conn.getresponse()#获取返回内容对象
	data = response.read()#从对象中读取数据
	if data:
		print 'recev data'
		f = open('aa.txt','write')
		f.write(data)#把返回结果输入到文本文件中
	else :
		print 'no data'
   	time.sleep(0.1)#休息0.1秒后关闭连接
	conn.close() 
if __name__ == '__main__':
#	a = 1
#	while 1:
		send()
	#	a=a+1
	#	print a
	
