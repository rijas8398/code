'''hrs = int(input("Enter hours:"))
rate = float(input("Enter rate:"))
pay = float(hrs*rate)
print('pay:',pay)

Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
h = float(hrs)
pay = h * 10.50
if (h <= 40):
    print(pay)
else:
    pay = (40 + 1.5*(h-40))*10.50
    print(pay)

score = input("Enter Score: ")
s = float(score)
if s>1.0 or s<0:
    print("score is out of range")
elif s>=.9:
    print("A")
elif s>=.8:
    print("B")
elif s>=.7:
    print("C")
elif s>=.6:
    print("D")
elif s<.6:
    print("F")
else:
    print("score is out of range")
    quit()

score = input("Enter Score: ")
s = float(score)
grade=''
if s>1.0 or s<0:
    print("score is out of range")
elif s>=.9:
    grade = 'A'
elif s>=.8:
    grade = 'B'
elif s>=.7:
    grade = 'C'
elif s>=.6:
    grade = 'D'
elif s<.6:
    grade = 'F'
else:   
    print("score is out of range")
    quit()
print(grade)
a='456'
d=int(a)
b=d+1
print(b)

def mkr():
    return "rijas"
print(mkr(),'evide')

def computepay(h,r):
    if h <= 40 :
        pay=h*r
    else:
        pay=h*r + (h-40)*(r/2)
    return pay

hrs = input("Enter Hours:")
h=float(hrs)
rate=input("Enter rate:")
r=float(rate)
p = computepay(45,10.50)
print("Pay",p)

count=0
avg=0
sum=0
for value in [0,45,12,78,3,5,98,41] :
    count+=1
    sum+=value
print("avg is",sum/count)
smallest=None
#none means no value in it (equals to '')
for value in [45,25,7,3,1,98,65,78]:
    if smallest is None :
        smallest=value
    elif value < smallest :
        smallest=value
    print(smallest,value)
print('after',smallest)

count=0
tot=0
while True:
    aval=input("enter a number:")
    if aval=='Done':
        break
    try:
        bval=float(aval)
    except:
        print('invalid input')
        continue
    count=count+1
    tot=tot+bval
print(tot,count,tot/count)


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
       validnum=float(num)
    except:
        print('invalid input')
        continue
    if smallest is None:
        smallest=validnum
    elif validnum < smallest:
        smallest=validnum
    if largest is None:
        largest = validnum
    elif validnum > largest:
        largest = validnum

print("Maximum", largest)
print("minimum",smallest)


name="mohamed rijas"
print(name[0:4])
print(name[1:4])
print(name[:9])
print(name[5:])
print(name[:])

str='rijas mk'
type (str)
print(type)
print(dir(str))
new=str.replace('rijas','mkr')
print(new)
str1='   efeh ed     '
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())
print(str.startswith('r'))
print(str.startswith('R'))

email="mohamedrijasmk.mec@gmail.com"

at=print(email.find('@'))
dot=print(email.find('.'))
college=print(email[15:18])
dot2=print(email.find('.',at))

text = "X-DSPAM-Confidence:    0.8475";
zero=text.find('0')
num=text[23:]
number=float(num)
print(number)

fh = open("romeo.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    print(line.upper().strip())

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
floatvalue = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    count += 1
    zero = line.find('0')
    floatvalue += float(line[zero:])
print('Average spam confidence:', float(floatvalue / count))
s = [ 4, 8, 1, 3]
s.reverse()
print(s)

s.sort()
print(s)
s.append(7)
print(s)
4 in s

print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(sum(s)/len(s))

man='there is a man on the beach'
listm=man.split()
print(listm)
print(len(listm))
print(listm[3])

line='edced;cerde3;ceec'
l1=line.split()
print(l1)
l2=line.split(';')
print(l2)

line='hee@cjhbd dedd cdhcdsbc'
data=line.split()
print(data)
word=data[0]
print-(word)
email=word.split('@')
print(email)
eid=email[1]
print(eid)

#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    words=line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

    lst.sort()

print(lst)
#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line.rstrip()
    if not line.startswith('From '):
        continue
    count+=1
    words=line.split()
    print(words[1])


print("There were", count, "lines in the file with From as the first word")

d=dict()
d['phone'] = 7559051416
d['age'] = 21
d['age'] = 22
print(d)

dd={'a': 10 , 'b' :25 , 'c': 50}
print(dd)

counts=dict()
names=['rijas','mkr','mkr','rijas','mkrijas','rijas']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)

counts=dict()
print('enter a line of text:')
line=input('')
words=line.split()
print('words is',words)
for word in words:
    counts[word]=counts.get(word,0)+1
print(counts)

dd={'a': 10 , 'b' :25 , 'c': 50}
print(list(dd))
print(dd.keys())
print(dd.values())
print(dd.items())

for k,v in dd.items() :
    print(k,v)


name=input('enter a file:')
handle=open(name)

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount=count
print(bigword,bigcount)

#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
for line in handle:
    line.rstrip()
    if line.startswith('From '):
        words=line.split()
        email=words[1]
        lst.append(email)

dct=dict()
for email in lst:
    dct[email] = dct.get(email,0) + 1

email_address=None
bigcount=None

for key,value in dct.items():
    if email_address is None or value > bigcount:
        email_address=key
        bigcount=value

print(email_address,bigcount)


(m,k)=(8,3)
print(k)
 (78,14)<(154,3)
 #list of two tuples [(2,4),(85,47)]


jdd={'asxh': 10 , 'trjkb' :25 , 'zjnkdc': 50}
print(jdd.items())
print(sorted(jdd.items()))

dd={'asxh': 28 , 'trjkb' :7 , 'zjnkdc': 50}
lst=list()
print(dd.items())

for k,v in dd.items():
 lst.append((v,k))

print(lst)
print(sorted(lst,reverse=True))

#To find top 10 most commom words:


name=input('enter a file:')
handle=open(name)

dd=dict()
for line in handle:
    words=line.split()
    for word in words:
        dd[word]=dd.get(word,0)+1

lst=list()
key,value in dd.items():
 tup=(value,key)
 lst.append(tup)

lst=sorted(lst,reverse=True)
for value,key in lst[:10]:
 print(key,value)

#shorter version: list comprehension:

print(sorted([(value,key) for (key,value) in dd.items()]))

name=input('enter a file:')
handle=open(name)

dd=dict()
for line in handle:
    words=line.split()
    for word in words:
        dd[word]=dd.get(word,0)+1

print(sorted([(value,key) for (key,value) in dd.items()]))

for value,key in lst[:10]:
 print(key,value)

#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()

for line in handle:
    line.rstrip()
    if line.startswith('From '):
        words=line.split()
        time=words[5]
        t=time.split(':')
        hour=t[0]

        count[hour]=count.get(hour,0) + 1

lst=list()
for k,v in count.items():
    tup=(k,v)
    lst.append((k,v))

lst=sorted(lst)
for k,v in lst:
    print (k,v)





#"REGULAR EXPRESSION"
#you can use regular expression in your language by using "import re"
#u can use "re.search() to see if a string matches a regular expression.similar to using find() method for strings"
# use re.findall()  to extract portions of string that matches your r e,similar to combination of find() and slicing: var[5:10]

#"HACKERRANK":

n=int(input("enter size of array"))
sum=0
ar=
for i in range(n):
    ar.append((i))
    sum+=i
print(sum)


print(abs(4-6))

(input())
def plusMinus(arr):
    positive=0
    neghative=0
    zero=0
    fraction=0
    for elm in arr:
        if elm>0:
            positive+=1
        elif elm<0:
            neghative+=1
        else:
            zero+=1
    pf=(positive/len(arr))
    nf=(neghative/len(arr))
    zf=(zero/len(arr))
    print(pf,nf,zf)
def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end='')

        print("\r")
result = pypart(4)
print(result)

def pyrmid(n):
    k = 2*n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1

        for j in range(0,i+1):
            print("*",end="")
        print("\r")
result = pyrmid(5)
print(result)
#using rjust function:
def staircase(n):
    for i in range(1, n + 1):
        print(('#'*i).rjust(n))
result=staircase(5)
print(result)


def printPalindrome(n):
    if (n == 1):
        print("Smallest Palindrome: 0")
        print("Largest Palindrome: 9")
    else:
        print("Smallest Palindrome:", int(pow(10, n - 1)) + 1)
        print("Largest Palindrome:", int(pow(10, n)) - 1)


result=printPalindrome(5)
print(result)



print(10==4)
print(8<7)
print(108>54)
print(bool("rijas"))
print(bool(25))
print(bool("51rijas"))
print(bool("rijas">"yjv"))
print(bool("rijas">"agdefe"))

n=input("enter the seconds to convert:")

total_seconds=int(n)


hour=total_seconds // 3600
seconds_remaining=total_seconds % 3600
minutes=seconds_remaining //60
seconds=seconds_remaining %60

print("hour",hour,"minutes",minutes,"seconds",seconds)

s='14sxsxwxs4'
print(int(s[0:2])+5)'''


def timeConversion(s):
    if s[8:] == 'PM':
        if int(s[:2]) < 12:
            return str(int(s[:2]) + 12) + str(s[2:8])
        else:
            return s[:8]


    else:
        if int(s[:2]) == 12:
            return '00' + str(s[2:8])
        else:
            return s[:8]
