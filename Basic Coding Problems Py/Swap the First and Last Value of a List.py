n=int(input("enter the number of elements: "))
a=[]
for i in range(n):
    b=int(input("enter element "))
    a.append(b)
print(a)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp_
print(a)
