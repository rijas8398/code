def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end='')

        print("\r")



result = pypart(4)
print(result)

def countnum(n):
    num = 1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num, end=" ")
            num += 1
        print("\r")

result = countnum(5)
print(result)

def pyletter(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=' ')
            num += 1
        print("\r")

result = pyletter(5)
print(result)


def pyletter(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=' ')
        num += 1
        print("\r")

result = pyletter(5)
print(result)

def countnum(n):
    num = 1
    for i in range(0,n):
        num = 1
        for j in range(0,i+1):
            print(num, end=" ")
            num += 1

        print("\r")

result = countnum(5)
print(result)

def pyletter(n):
    num = 65
    for i in range(0, n):
        num = 65
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=' ')
            num += 1
        print("\r")

result = pyletter(5)
print(result)

def pyrev(n):
    k = 2*n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 2

        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
result = pyrev(5)
print(result)


def pyrmid(n):
    k = 2*n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1

        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
result = pyrmid(5)
print(result)

