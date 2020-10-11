import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', type = int)

    return parser

def fibonacci(n):
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

parser = createParser()
namespace = parser.parse_args()

print(fibonacci(namespace.n))
