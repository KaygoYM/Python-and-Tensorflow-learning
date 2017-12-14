#sharing cpu inside
import multiprocessing as mp
import time

def job(v,num,l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        va.value+=num#内存摄取
        print(va.value)
    l.release()


def multicore():
    va=mp.Value('i',0)#i形态
    #类似于全变量
    l=mp.Lock()
    p1=mp.Process(target=job,args=(va,1,l))
    p2=mp.Process(target=job,args=(va,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__=='__main__':
    multicore()


#array=mp.Array('i',[45,6,7,88,9])#只能是一维
