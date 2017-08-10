# -*- coding:utf-8 -*-
#!/usr/bin/env python

#创建一个 Thread 的实例，传给它一个可调用的类对象
import threading
from time import ctime, sleep

loops = [4,2]

class ThreadFunc(object):
    
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args
        
    def __call__(self):
        apply(self.func, self.args)
        
def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    
def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i,loops[i]), loop.__name__))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()  #start all threads
        
    for i in nloops:
        threads[i].join()  #wait for completion
        
    print 'all DONE at:', ctime()
    
if __name__ == '__main__':
    main()
        
        