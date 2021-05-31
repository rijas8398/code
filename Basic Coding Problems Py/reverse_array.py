def reverse(s,start,end):

    while(start<=end):
        print(s[start], s[end])
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1
    return s
s="rijasmk"
s=list(s)
print(reverse(s,0,len(s)-1))

T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    start = 0
    end = N - 1
    while (start <= end):
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    print(' '.join(str(i) for i in A))
