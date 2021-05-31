'''n=int(input("enter the number of elements: "))
a=[]
for i in range(n):
    b=int(input("enter element "))
    a.append(b)
print(a)
a.sort()
print(a[-2])'''

a=[1,8,9,6,5,7]
n=len(a)

first=a[0]
second=a[1]
if a[0] > a[1]:
    first = a[0]
    second=a[1]
elif a[0] < a[1]:
    first = a[1]
    second=a[0]
    
for i in range(2,n):
    if a[i]>first:
        second=first
        first=a[i]

    elif a[i]>second and a[i]!=first:
        second=a[i]
print(first,second)

