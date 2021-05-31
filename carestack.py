'''
def palindrome(s):
    str=''
    for ele in s:
        str=ele+str

    if (str==s):
        print("it's a palindrome")
    else:
        print("it is not a palindrome")
    return
palindrome("malayalam")


s="Malayalam"
n=len(s)
s=s.lower()
if s==s[::-1]:
    print("it is palindrome")
else:
    print(" not ")

def check(s):
    if s[0]=="f" and s[len(s)-1]=="d":
        print("true")
    else:
        print("false")
s="findr"
check(s)
'''
def check(s):
    flag = 0
    for i in range(len(s)):

        if s[i]=="a":
            if s[i+1]=="a":
                print("true")
                flag=1
                break

    if flag==0:
        print("false")



s="Factback"
check(s)

