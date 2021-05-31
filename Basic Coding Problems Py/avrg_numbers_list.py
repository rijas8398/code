n=int(input("enter no of elements to be inserted: "))
lst=[]
sum=0
for i in range(n):
    m=int(input("enter the elements: "))
    lst.append(m)
    sum+=m
print(lst)
avg=sum/n
print("average is ",avg)
