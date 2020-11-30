from time import time
from random import randint, sample
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue



def scal_mul(v1, v2):
    res = 0
    for (i, j) in zip(v1, v2):
        res += i*j
    return res

def mul(x, y):
    return x*y

res = 0

def compute_sum(q, n = 8):
    global res
    for _ in range(n):
        res += q.get()
    return res


def scal_mul_proc(v1, v2, n = 8): #n добавим чтобы установить кол-во процессов
    q = Queue()
    procs = [Process(target = q.put, args = (v1[i]*v2[i], )) for i in range(n)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    return compute_sum(q, n)


if __name__ == "__main__":

    v1, v2, v3, v4 = [randint(0, 10000) for i in range(10)], [randint(1000, 100000000) for i in range(100)], [randint(1000000, 10000000000000000) for i in range(1000)], [randint(10000000000, 100000000000000000000) for i in range(10000)]
    vector_len = [10, 100, 1000, 10000]

    print('random generation ended')

    jobtime = {'simple':[], 'with_threads':[]}

    for (u, v) in (v1, sample(v1, k = 10)), (v2, sample(v2, k = 100)), (v3, sample(v3, k = 1000)), (v4, sample(v4, k = 10000)):

        for f in (scal_mul, scal_mul_proc):
            runtime = 0
            for i in range(3):
                start = time()
                f(u, v)
                end = time() - start
                runtime += end

            jobtime['simple'].append(runtime/3) if f is scal_mul else jobtime['with_threads'].append(runtime/3)


    print(jobtime)

    plt.plot(jobtime['simple'], vector_len)
    plt.plot(jobtime['with_threads'], vector_len)
    plt.grid(True)
    plt.show()
