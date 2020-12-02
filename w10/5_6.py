import threading
from time import time
from random import randint
from multiprocessing import Process
#import matplotlib.pyplot as plt

#thats a lot of garbage
#please DO NOT run this code it will fuck your computer

def scal_mul(v1, v2):
    res = 0
    for i, j in zip(v1, v2):
        res += i*j
    return res

'''
def alt_mul(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += v1[i]*v2[i]
    return res
'''

lock = threading.Lock()
res = 0

def mul(x, y):
    return x*y

def component_mul(x, y):
    global res
    lock.acquire()
    res += x*y
    lock.release()



def scal_mul_threads(v1, v2):
    for i in range(len(v1)):
        thread = threading.Thread(target = component_mul, args = (v1[i], v2[i]))
        thread.start()
    return res




if __name__ == "__main__":

    how_many_procs = [2, 4, 6, 8]
    n = 2

    def scal_mul_proc(v1, v2, n = 8): #n добавим чтобы установить кол-во процессов
        procs = []
        for i in range(len(v1)):
            proc = Process(target = mul, args = (v1[i], v2[i]))
            procs.append(proc)
        #теперь у меня есть массив процессов - бери и запускай
        i = 0
        while i <= n and procs != []:
            for p in procs[:n]:
                p.start()
            for p in procs[:n]:
                p.join()
            procs = procs[n:]

            if i == n:
                i = 0
            else:
                i += 1
        return res


    v1, v2 = [randint(10000000000, 100000000000000000) for i in range(10000)], [randint(10000000000, 100000000000000000000) for i in range(10000)]

#    print(scal_mul_proc(v1, v2))
    print(scal_mul(v1, v2))

    print('random generation ended')
    '''
    proc_mul_job = []

    for n in how_many_procs:
        start = time()
        scal_mul_proc(v1, v2, n)
        end = time() - start
        proc_mul_job.append(end)
    '''

    print(scal_mul_proc([1, 2, 3, 4, 555, 6], [9, 8, 67, 88, 7, 6]))
    print(scal_mul([1, 2, 3, 4], [9, 8, 7, 6]))




'''

    for f in (scal_mul, scal_mul_threads):
        for i in range(3):

            start = time()
            f(v1, v2)
            end = time() - start
            jobtime.append(end)

    print(*jobtime)
'''
