from itertools import product

def get_cartesian_product(a, b):
    yield product(a, b)
