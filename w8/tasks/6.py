from itertools import combinations


def get_combinations(s, k):
    a = [''.join(sorted(x)) for i in range(1, k + 1) for x in combinations(s, i)]
    a.sort(key = lambda x: len(x))
    return a
