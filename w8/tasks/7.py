from itertools import groupby


def compress_string(s):
    a = []
    for key, value in groupby(s):
        a.append((len(list(value)), key))
    return a

#print(compress_string('1222311'))
