import threading
from queue import Queue
import copy
import time

def job1():
    #print('job1 start\n')
    global A,lock
    lock.acquire()
    for _ in range(10):
        A+=1
        print('job1 finish and A is',A,'\n')
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    #print('job2 start\n')
    for _ in range(10):
        A+=10
        print('job2 finish and A is',A,'\n')
    lock.release()
    

def job(l,q):
    print('start the job\n')
    res=sum(l)
    q.put(res)
    print('finish the job\n')


def multithreading(l):
    q=Queue()
    threads=[]
    for i in range(4):
        t=threading.Thread(target=job,args=(copy.copy(l),q),name='T%i'%i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total=0
    for _ in range(4):
        total+=q.get()
    print(total)


def normal(l):
    total=sum(l)
    print(total)


if __name__=='__main__':
    l=list(range(10))
    s_t=time.time()
    normal(l*4)
    print('normal:',time.time()-s_t)
    s_t=time.time()
    multithreading(l)
    print('multithreading:',time.time()-s_t)


    lock=threading.Lock()
    A=0#全局变量
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
