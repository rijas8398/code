l1=[1,2,3,1,2,4]
l2=[5,2,1,6,2,4,4]
d1 = {}
d2 = {}
for ele in l1:
    if ele not in d1:
        d1[ele] = 1
    else:
        d1[ele] += 1

for ele in l2:
    if ele not in d2:
        d2[ele] = 1
    else:
        d2[ele] += 1

print(d1)
print(d2)

arr=[ ]
for ele in d1:
    if ele in d2:
         arr.extend(str(ele)*min(d1[ele] , d2[ele]))


print(arr)

