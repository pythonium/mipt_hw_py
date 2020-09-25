
A = list(map(int, input.split()))
N = len(A)

#A.sort() и A = sorted(A)

#пузырьком
def bubble(A):
    for i in range(N-1):
        for j in range(N-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A
