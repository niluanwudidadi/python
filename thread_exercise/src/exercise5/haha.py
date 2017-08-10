# -*- coding:utf-8 -*-
#!/usr/bin/env python

#从 Thread 派生出一个子类，创建一个这个子类的实例
import threading
from time import ctime, sleep

loops = [4,2]

class MyThread(threading.Thread):
    
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        
#     def getResults(self):
#         return self.res
        
    def run(self):
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
        t = MyThread(loop, (i,loops[i]), loop.__name__)
        threads.append(t)
    
    for i in nloops:
        threads[i].start()  #start all threads
        
    for i in nloops:
        threads[i].join()  #wait for completion
        
    print 'all DONE at:', ctime()
    
if __name__ == '__main__':
    main()
        
        