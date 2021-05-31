
name=['baby','delli','putti','muthutty','putti']
tup=tuple(name)
print(tup)
lst=list(tup)
print(lst)
sett=set(lst)
print(sett)
print(tup[0])
lst[0]='singh'
tup[0]=='singh' #doesn't work

print(lst)
print(tup)
print(sett)

string_name=' '.join(name)
print(string_name)

#reverse by words

words=string_name.split()
reverse_string=' '.join(reversed(words))
print(reverse_string)

# to count the occurrences of a particular element in the list
name=['baby','delli','putti','muthutty','putti']
print(name.count('putti'))

print([[x,name.count(x)] for x in set(name)])


a=[4,5,7,8,9]
print(a[-1])
print(a[0])
print(a[-3])
print(a[::-1])
print(a[::2])
print(a[::-2])
print(name[-1][-2])

subjects = ('Python', 'Interview', 'Questions')
for i, subject in enumerate(subjects):
    print(i, subject)

subjects = ['Python', 'Interview', 'Questions']
for i in range(len(subjects)):
    print(i, subjects[i])

subjects = ('Python', 'Interview', 'Questions')
for i in range(len(subjects)):
    print(i, subjects[i])

print(sum(range(1,101)))

print (range(1,101))

lst=[4,5,6]
print(lst*2)

print(list('hello'))
#use of round function
print(round(46.235,2))


