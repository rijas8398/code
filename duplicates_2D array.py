names=['ball','box','stack','ball','box']
price=[1,3,1,1,3]
weight=[1,2,5,1,2]

def duplicates(names,price,weight):
    d={}

    for i in range(len(names)):
        x=(names[i],price[i],weight[i])
        print(x)

        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    return d

dic = duplicates(names, price, weight)
print(dic)
count = 0
for key in dic:
    if dic[key] > 1:
        count += dic[key] - 1
print(count)
