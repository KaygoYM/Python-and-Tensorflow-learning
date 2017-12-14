#multiprocessing
import multiprocessing as mp
#import threading as td

def job(q,a,b):
    print('a+b=',a+b)
    q.put(a+b)#从queue输出返回值


#pool
def job2(x):
    return x**2#有返回值了！

def multicore():
    pool=mp.Pool()#(processes=3)用三个核
    result=pool.map(job2,range(10))
    print(result)
    result2=pool.apply_async(job2,(2,))#无法输入大于1个的参数
    print(result2.get())

    multi_res=[pool.apply_async(job2,(i,)) for i in range(10)]
    print([result3.get() for result3 in multi_res])
    
if __name__=='__main__':
    #t1=td.Thread(target=job,args=(1,2))
    q=mp.Queue()

    p1=mp.Process(target=job,args=(q,2,3))
    p2=mp.Process(target=job,args=(q,3,3))#args=(q,)

    #t1.start()
    p1.start()
    p2.start()
    #t1.join()
    p1.join()
    p2.join()

    res=[]

    for i in range(q.qsize()):
        res.append(q.get())
    print(res)


    multicore()
