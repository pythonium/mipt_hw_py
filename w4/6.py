def swap(f):
    def wrapper(*args, **kwargs):
        args = reversed(args)
        f(*args, **kwargs)
    return wrapper

def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show = True)
swapped = swap(div)
swapped(2, 4, show = True)

'''
или так
@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)
'''
