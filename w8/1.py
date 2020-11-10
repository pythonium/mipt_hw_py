def some_func(x):
    return f"я какая-то функция, я возвращаю {x}"

def print_map(function, iterable):
	print(*(map(function, iterable)), sep = '\n')


print_map(some_func, [1, 2, 3, 4])
