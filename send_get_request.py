#!/usr/bin/env python
#coding:utf-8
import httplib, urllib
import datetime
import time
'''
函数名：send
作用：给OA发送get请求
'''
def send():
	conn = httplib.HTTPConnection('172.16.17.101')#连接主机
	conn.request('GET','/oa/main/errorindex')#发送get请求
	r1 = conn.getresponse()
	print r1.status,r1.reason
	conn.close()
if __name__ == '__main__':
	a=1
	while 1:
		send()
		a = a+1
		print a
