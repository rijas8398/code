def getMinMax(a, n):
    if a[0]>a[1]:
        max=a[0]
        min=a[1]
    elif a[0]<a[1]:
        max=a[1]
        min=a[0]


    for ele in range(2,n):
        if a[ele] > max:
            max = a[ele]

        elif a[ele] < min:
            min = a[ele]
    return (min, max)
a=[45,26,8,93,45]
n=5
result=getMinMax(a,n)
print(result)