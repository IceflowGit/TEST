#!/usr/bin/env python
#-*-coding:utf-8-*-
import threading
from time import sleep,ctime
loops = [4,2]
def loop(loop_count,sleep_time):
	print 'start loop',loop_count,'at:',ctime()
	sleep(sleep_time)
	print 'stop loop',loop_count,'at:',ctime()

threads = []
def main():
	print 'starting at:',ctime()
	thread = []
	nloops = range(len(loops))
	for i in nloops:
		t = threading.Thread(target=loop,args=(i,loops[i]))
		threads.append(t)
	for i in nloops:
		threads[i].start()
	for i in nloops:
		threads[i].join()
if __name__=='__main__':
	main()

