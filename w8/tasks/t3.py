def my_map(function, iterable):
	for i in iterable:
		yield function(i)

def my_enumerate(iterable, start = 0):
	for i in iterable:
		yield start, i
		start += 1

def my_zip(*iterables):
	minlen = min(list(map(len, iterables)))
	for i in range(minlen):
		yield tuple(j[i] for j in iterables)
