n=int(input("enter the number of elements: "))
a=[]
for i in range(n):
    b=int(input("enter element "))
    a.append(b)
print(a)
a.sort()
i=0
while (i<len(a)-1):

    if a[i]==a[i+1]:
        del(a[i])
    else:
        i+=1

print(a)

