'''s1=input("enter frst string: ")
s2=input("enter 2 nd no: ")
lst=list(set(s1) & set(s2))
for ele in lst:
    print(ele)'''

s1=input("enter frst string: ")
s2=input("enter 2 nd string: ")
a=list(s1)
b=list(s2)
print(a)
print(b)
d={}
for ele in a:
    if ele in b:
        d[ele]=1
print(list(d.keys()))



