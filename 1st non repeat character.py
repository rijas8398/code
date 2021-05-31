def non_rpt(s):
    d={}
    for ele in s:
        if ele not in d:
            d[ele]=1
        else:
            d[ele]+=1
    for key in d:
        if d[key]==1:
            print(key)
            break


result=non_rpt('malayalam')
print(result)