def fib_gen(n):
    if n > 0:
        a = 1
        yield a

        if n > 1:
            b = 1
            yield b

            if n > 2:
                k = 2

                while k < n:
                    yield a + b
                    a, b = b, a+b
                    k += 1

print(*fib_gen(8))
