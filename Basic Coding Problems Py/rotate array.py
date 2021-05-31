T=int(input())
for i in range(T):
    N,D=tuple(map(int,input().split()))
    arr=list(map(int,input().split()))
    l=[]
    l=arr[D:]+arr[:D]
    print(' '.join(str(j) for j in l))