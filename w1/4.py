#вариант1
A = []
i = 1
j = 9
while j*j < 2500:
    A.append(i*i)
    A.append(j*j)
    i += 10
    j += 10

print(A)

#вариант 2
B = []
for i in range(50):
    if (i*i) % 10 == 1:
        B.append(i*i)

print(B)