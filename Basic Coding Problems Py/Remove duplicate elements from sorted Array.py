def remove_duplicate(self, A, N):
    end = 0
    for i in range(N - 1):
        if A[i] != A[i + 1]:
            A[end] = A[i]
            end += 1
    A[end] = A[N - 1]
    return end + 1
