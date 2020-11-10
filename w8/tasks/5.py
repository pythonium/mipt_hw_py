from itertools import permutations


def get_permutations(s, n):
    return sorted([''.join(x) for x in permutations(s, n)])


#print(get_permutations("cat", 2))
