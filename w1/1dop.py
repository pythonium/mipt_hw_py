A = list(map(int, input().split()))
B = []
while A != []:
    B.append(A[0]+A[-1])
    A.pop(0)
    if A != []:
        A.pop()

print(B)


