# Неделя 4
_________
### sys
1.Напишите программу, которая выводит количество переданных ей аргументов и печатает питоновский list, состоящий из этих аргументов.

```python
import sys

print(sys.argv)
print(len(sys.argv) - 1)
```
In: ```python3 1.py 22 33 44 ```

Out:
```python
['1.py', '22', '33', '44']
3
```
2.Напишите программу, которая выводит версию питона и используемое ядро ОС.
```python
import sys

print(sys.version)
print(sys.platform)
```

```python
3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 23:10:23) [MSC v.1927 64 bit (AMD64)]
win32
```
### argparse
3. Напишите консольную программу, которой на вход подается единственное число N (без имени или с именем -n), а программа печатает значение Nго числа Фибоначчи.
Использовать `argparse`.

```python
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
```
In: ```python3 3.py -n 8```

Out: ``` 21```

4. Напишите программу, которая на вход принимает три аргумента `--show-all (-a)`, `--file (-f) <file>` и один позиционный `number` и выводит n-ое простое число.
Если передан аргумент командной строки `--show-all` или `-a`, то необходимо показывать все предыдущие простые числа (иначе показать только последнее).
Если передан `--file` или `-f`, то нужно сохранить вывод программы в файл помимо печати в консоль (естественно, после `--file` надо считать путь к файлу).
Порядок именованных аргументов не должен иметь значения.
Для чтения файла использовать `argparse.FileType()`.

```python
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
```

In: ```python3 4.py 8 -a```

Out:
```python
23
2 3 5 7 11 13 17 19 23
```
In:```python3 4.py 8 -a -f 4.txt```

4.txt:
```python
2
3
5
7
11
13
17
19
23
```
### декораторы
5. Напишите функцию, которая получает на вход список чисел и выдает ответ, сколько в данном списке четных чисел.
Напишите декоратор, который меняет поведение функции следующим образом: если четных чисел нет, то пишет "Нет(" а если их больше 10, то пишет "Очень много".
```python
def even(arr):
	s = 0
	for i in arr:
		if i % 2 == 0:
			s += 1
	return s


def dec(f):
	def wrapper(arr):
		s = even(arr)
		if s == 0:
			return("нет")
		elif s > 10:
			return("очень много")
		else:
			return s
	return wrapper

neweven = dec(even)

a = [i for i in range(100)] # >10 четных
b = [1, 3]                  #нет четных
c = [i for i in range(10)]  #не много четных

print("even(a) = ", even(a), " neweven(a) = ", neweven(a))
print("even(b) = ", even(b), " neweven(b) = ", neweven(b))
print("even(c) = ", even(c), " neweven(c) = ", neweven(c))
```
Out:
```python
even(a) =  50  neweven(a) =  очень много
even(b) =  0  neweven(b) =  нет
even(c) =  5  neweven(c) =  5
```
6. Напишите декоратор `swap`, который делает так, что задекорированная функция принимает все свои неименованные аргументы в порядке, обратном тому, в котором их передали (для аргументов с именем не вполне правильно учитывать порядок, в котором они были переданы).

```python
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
```
Out:
```python
0.5
2.0
```
7. Напишите декоратор, который принимает в качестве аргумента путь к файлу. Если данный декоратор добавить к функции, то в указанный файл будет логироваться информация вида:
    - Время вызова функции
    - Входящие аргументы
    - Ответ return (если есть, если нет то логгировать '-')
    - Время завершения работы функции
    - Время работы функции
    
```python
import time
from datetime import datetime
from functools import wraps

def logger(file):
	def dec(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			start = time.time()
			f(*args, **kwargs)
			stop = time.time()
			timeinwork = stop - start
			start, stop = datetime.fromtimestamp(start), datetime.fromtimestamp(stop)
			returned = f(*args, **kwargs) if f(*args, **kwargs) is not None else '-'

			with open(file, "w") as log:
				log.write(
				"called at {}\narguments: {}\nreturned: {}\nended at: {}\nexecution time:{}\n".format(start, args, returned, stop, timeinwork))

			return f(*args, **kwargs)
		return wrapper
	return dec

@logger("log.txt")
def func(a, b):
        return a + b

func(1, 2)
```
log.txt:
```python
called at 2020-10-11 22:40:42.666924
arguments: (1, 2)
returned: 3
ended at: 2020-10-11 22:40:42.668912
execution time:0.0019881725311279297