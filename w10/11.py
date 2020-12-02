from time import time
from random import randint
from multiprocessing import Process, Pool


def scal_mul(v1, v2):
    res = 0
    for i, j in zip(v1, v2):
        res += i*j
    return res


def mul(x, y):
    return x*y

if __name__ == "__main__":
    def scal_mul_pool(v1, v2):
        pool = Pool(processes = 4)
        results = [pool.apply(mul, args = (i, j)) for i, j in zip(v1,v2)]
        return(sum(results))

#    v1, v2 = [randint(1, 20) for i in range(15)], [randint(1, 20) for i in range(15)]
#    print(scal_mul(v1, v2))
#    print(scal_mul_pool(v1, v2))
