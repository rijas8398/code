n=int(input("enter the number :"))
sq_Sum=0
while(n>0):
    rem=n%10
    sq_Sum+=rem**2
    n=n//10
print("sum of square of digits is " + str(sq_Sum))


