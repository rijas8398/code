n=int(input("enter the number of elements: "))
a=[]
for i in range(n):
    b=int(input("enter element "))
    a.append(b)
print(a)
d={}
for ele in a:
    if ele not in d:
        d[ele]=1
    else:
        d[ele]+=1
for ele in d:
    if d[ele]>1:
        print(ele,end=' ')