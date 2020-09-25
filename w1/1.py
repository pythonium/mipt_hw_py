
from math import sqrt
x = input()
n = 0
sum = 0
sumquad = 0
min = int(x)
max = int(x)

while x != 'end':
    x = int(x)
    n += 1
    sum += x
    sumquad += x*x

    if x > max:
        max = x
    if x < min:
        min = x

    x = input()

avg = sum/n
S = sqrt((sumquad - 2*avg*sum)/n + avg*avg)   #просто раскрыла формулу
print(max, min, avg, S)