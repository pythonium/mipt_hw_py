import threading
from time import time
from random import randint

#thats a lot of garbage

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


v1, v2 = [randint(10000000000, 100000000000000000) for i in range(10000)], [randint(10000000000, 100000000000000000000) for i in range(10000)]


print('random generation ended')
start = time()
scal_mul_threads(v1, v2)
end = time() - start
print(end)
start, end = 0, 0
start1 = time()
scal_mul(v1, v2)
end1 = time()
print(end1 - start1)

#какого ... без тредов работает быстрее
