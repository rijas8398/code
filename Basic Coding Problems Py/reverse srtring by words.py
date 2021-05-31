'''
def re_words(string):
    words=string.split(' ')
    print(words)
    re_string=' '.join(reversed(words))
    print(re_string)
re_words('my name is rijas')
'''

#How to reverse the string but not the words in it
strr="hello my name is Rijas mk "
s=strr[::-1]
print(s)
temp=""
for ele in strr.split():
    print(ele)
    temp+=ele[::-1]
    temp+=" "
    print(temp)
print(temp)
print(temp.join(""))



