#!/usr/bin/env python
#-*-coding:utf-8-*-
from time import sleep,ctime
import thread
def loop0():
	print 'start loop 0 at:',ctime()
	sleep(4)
	print 'loop0 done at:',ctime()

def loop1():
	print 'start loop 1 at:',ctime()
	sleep(2)
	print 'loop1 done at:',ctime()

def main():
	print 'starting at:',ctime()
	thread.start_new_thread(loop0,())
	thread.start_new_thread(loop1,())
	sleep(6)
	print 'all DONE at:',ctime()

if __name__=='__main__':
	main()
