'''def reverse(n):
    print("original number is",n)
    num=''
    for ele in n:
        num=ele+num
    print("reversed string is",num)

reverse('12345')'''

def reverse(n):
    reverse=0
    while(n>0):
        rem=n % 10
        reverse=reverse*10+rem
        n=n//10
    print(reverse)
reverse(7895)
