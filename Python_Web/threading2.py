import threading
import time
from queue import Queue
def thread_job():
    print('T1 has launched\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 has finished\n')

def T2_job(l,q):
    print('T2 start\n')

    for i in range(len(l)):
        l[i]=l[i]**2
    q.put(l)    
    print('T2 finish\n')


def main():
    add_thread=threading.Thread(target=thread_job,name='T1')
    #thread2=threading.Thread(target=T2_job,name='T2')

    add_thread.start()
    #thread2.start()
    
    #thread2.join()
    add_thread.join()#等待add_thread运行完才继续，时间差
    
    print(threading.active_count())#激活了的线程数
    print(threading.enumerate())#激活的线程分别叫什么
    print(threading.current_thread())#目前的线程
    print('All done\n')

def multithreading():
    q=Queue()
    data=[[1,2,3],[3,6,6],[5,5,5],[7,8,9]]
    threads=[]
    for i in range(4):
        t=threading.Thread(target=T2_job,args=(data[i],q))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    results=[]
    for i in range(4):
        results.append(q.get())
    print(results)
        
if __name__=='__main__':
    main()
