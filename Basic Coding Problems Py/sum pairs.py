'''
def sumpairs(lst, sum):
    d = {}
    cnt = 0
    for ele in lst:
        if ele in d:
            cnt += d[ele]
            print(ele, sum - ele)

        else:

            d[sum - ele] = 1

    print(cnt)


lst = [2, 1, 5, 7, -1, 4, 4]

sumpairs(lst, 6)
'''
def sumpair(arr,k):
    lst=[]
    count=0
    for ele in arr:
        num=arr.pop()
        diff=k-num
        if diff in arr:
            lst.append((num,diff))
            arr.remove(diff)
            count+=1


    print(lst,count)
arr=[1,2,4,8,10,6,2,6]
k=12
sumpair(arr,k)