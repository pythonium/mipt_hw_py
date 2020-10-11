import math
import sys
import argparse

def createParser():
	parser = argparse.ArgumentParser()
	parser.add_argument('N', type = int)
	parser.add_argument('--show-all', '-a', action='store_true', default = False)
	parser.add_argument('--file', '-f', type = argparse.FileType('w'))

	return parser

def eratosthenes(n):
	n = int(1.5 * n * math.log(n))
	sieve = list(range(n + 1))
	sieve[1] = 0
	for i in sieve:
		if i > 1:
			for j in range(i + i, len(sieve), i):
				sieve[j] = 0

	sieve = list(filter(lambda x: x != 0, sieve))

	return sieve

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
primes = eratosthenes(namespace.N)
print(primes[-1])

if namespace.show_all:
	print(*primes)

	if namespace.file is not None:
		for i in primes:
			namespace.file.write(str(i) + '\n')
else:
	if namespace.file is not None:
		namespace.file.write(str(primes[-1]))
