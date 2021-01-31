import threading
from time import time
from random import randint, sample
import matplotlib.pyplot as plt


def scal_mul(v1, v2):
    res = 0
    for (i, j) in zip(v1, v2):
        res += i*j
    return res


def alt_mul(v1, v2): #когда по каким-то причинам выбрасывает ошибку в scal_mul
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

    v1, v2, v3, v4 = [randint(0, 10000) for i in range(10)], [randint(1000, 100000000) for i in range(100)], [randint(1000000, 10000000000000000) for i in range(1000)], [randint(10000000000, 100000000000000000000) for i in range(10000)]
    vector_len = [10, 100, 1000, 10000]

    print('random generation ended')

    jobtime = {'simple':[], 'with_threads':[]}

    for (u, v) in (v1, sample(v1, k = 10)), (v2, sample(v2, k = 100)), (v3, sample(v3, k = 1000)), (v4, sample(v4, k = 10000)):

        for f in (scal_mul, scal_mul_threads):
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
