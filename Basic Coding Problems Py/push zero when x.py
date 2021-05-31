#replace x with zeros anda dd it in the starting of array
'''
arr = [1, 2, 5, 2, 2, 8, 9]
n = 7
x = 2
count=0

for ele in arr:
    if ele == x:
        continue

    else:
        arr[count]=ele
        count+=1



arr=[]*(n-count)+arr[:count]
print(arr)
'''
#replace x with zeros and add it in the ending of array

arr = [1, 2, 5, 2, 2, 8, 9]
n = 7
x = 2
count=0

for ele in arr:
    if ele == x:
        continue

    else:
        arr[count]=ele
        count+=1

while(count<n):
    arr[count]=0
    count+=1
print(arr)




