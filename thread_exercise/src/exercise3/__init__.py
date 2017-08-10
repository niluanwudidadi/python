# -*- coding:utf-8 -*-
#！/usr/bin/env python

# 使用threading模块创建一个 Thread 的实例，传给它一个函数
import threading
from time import ctime, sleep

loops = [4,2]

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    
def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))
    
    #create threads
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
        
    #start threads
    for i in nloops:
        threads[i].start()
        
    #wait for all threads to finish
    for i in nloops:
        threads[i].join() #join()会等到线程结束，或者在给了 timeout 参数的时候，等到超时为止
    
    print 'all DONE at:', ctime()
    
if __name__ == '__main__':
    main()
        
    