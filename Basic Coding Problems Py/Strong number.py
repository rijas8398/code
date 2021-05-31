n=int(input("enter the number: "))
sum=0
temp=n
while (n>0):
    dig=n%10
    prod = 1
    while(dig>1):
        prod=prod*dig
        dig-=1
    sum+=prod
    n=n//10



if (sum==temp):
    print("it is strong no ")
else:
    print("it is not strong no")








