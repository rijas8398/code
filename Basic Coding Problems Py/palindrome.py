#string palindrome(using a variable)
def palindrome(s):

    str=''
    for ele in s:
        str=ele+str
    if (s==str):
        print(s+ " is a palindrome")
    else:
        print(s + " is not a palindrome")

palindrome('kottumala')
palindrome('malayalam')

#string palindrome(without a variable)
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")

'''
#check palindrme of a number

def palindrome(num):
    number=num
    reverse=0
    while(num>0):
        rem=num % 10
        reverse=reverse*10+rem
        num=num//10
    if (number==reverse):
        print(str(number)+ " is a palindrome")
    else:
        print(str(number) + " is not a palindrome")

palindrome(12321)
palindrome(8398)'''