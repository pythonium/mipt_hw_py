import threading
from time import time
from random import randint
from multiprocessing import Process

#thats a lot of garbage
#please DO NOT run this code it will fuck your computer

def scal_mul(v1, v2):
    res = 0
    for i, j in zip(v1, v2):
        res += i*j
    return res


def alt_mul(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += v1[i]*v2[i]
    return res


lock = threading.Lock()
res = 0


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

    def scal_mul_proc(v1, v2):
        procs = []
        for i in range(len(v1)):
            proc = Process(target = component_mul, args = (v1[i], v2[i]))
            procs.append(proc)
            proc.start()

        for p in procs:
            p.join()
        return res

    v1, v2 = [randint(10000000000, 100000000000000000) for i in range(10000)], [randint(10000000000, 100000000000000000000) for i in range(10000)]


    print('random generation ended')

    jobtime = []
    for f in (scal_mul, scal_mul_threads, scal_mul_proc):
        start = time()
        f(v1, v2)
        end = time() - start
        jobtime.append(end)

    print(*jobtime)
