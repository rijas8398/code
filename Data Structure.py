a = []
size=int(input("enter size :"))
for i in range(size):
    ele = int(input("enter the elements :"))
    a.append(ele)
print(a)

#insert a num at specified position:

num=int(input("enter the value to be inserted: "))
pos=int(input("enter position: "))

for i in range(size-1,pos-1,-1):
    a[i]=a[i-1]
    print(a)
a[pos]=num
size+=1
print(a)
