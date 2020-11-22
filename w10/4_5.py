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

'''
v1 = (1, 2, 3)
v2 = (4, 3, 2)
print(scal_mul(v1, v2))
'''


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

v1 = (115678901111, 245434557, 3435656877737,115678901111, 245434557, 3435656877737, 563424564687958779, 56324578, 56732458, 111651511111, 24543434535557, 343534535737, 563458779, 563424564687958779, 56324578, 56732458, 111651511111, 24543434535557, 343534535737, 563458779)
v2 = (115678901111, 245434557, 3435656877737, 563424564687958779, 56324578, 56732458, 111651511111, 24543434535557, 343534535737, 563458779, 44564873485686, 34575468468, 25234576476, 4523434567895678, 343445675567, 458867678, 11109876543111, 245434557, 34476747687935737, 563458779)

scal_mul(v1, v2)
scal_mul_threads(v1, v2)
'''
start = time()
scal_mul_threads(v1, v2)
end = time() - start
print(end)
start, end = 0, 0
start = time()
scal_mul(v1, v2)
end = time()
print(end - start)


for i in range(10):
    v1, v2 = [randint(0, 1000000000000) for i in range(10)], [randint(0, 1000000000000) for i in range(10)]

'''
