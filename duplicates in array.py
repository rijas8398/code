def duplicate(arr):
    d={}
    for ele in arr:
        if ele not in d:
            d[ele]=1
        else:
            d[ele]+=1
    for ele in d:
        if d[ele]>1:
            print(ele,end=' ')
    return

arr=[2,2,5,8,6,9,3,4,5,2]
result=duplicate(arr)
print(result)