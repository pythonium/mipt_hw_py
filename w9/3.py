import numpy as np

class Average(Exception):
    pass

class Dispersion(Exception):
    pass

class Quantity(Exception):
    pass

def coroutine():
    print('starting coroutine')
    data = []
    try:
        while True:
            try:
                x = yield
                data.append(x)
                avg = np.mean(data)
                dsp = np.var(data)
                qtt = len(data)
            except Average:
                yield avg
            except Dispersion:
                yield dsp
            except Quantity:
                yield qtt
    finally:
        print('stopping coroutine')



crt = coroutine()
next(crt)
for i in range(18):
    crt.send(i)
    if i % 3 == 0:
        print("current average:", crt.throw(Average))
        next(crt)

    if i % 2 == 0:
        print("current dispersion:", crt.throw(Dispersion))
        next(crt)

    if i % 4 == 0:
        print("Current count:", crt.throw(Quantity))
        next(crt)


crt.close()
