#try and except is used to remove errors in code.

'''try:
    number = int(input("enter a number: "))
    print(number)

except ZeroDivisionError :
    print("divided by zero")
except ValueError:
    print("invalid") '''
try:
    answer=50/0
    number = int(input("enter a number: "))
    print(number)

except ZeroDivisionError as err :
    print(err)
except ValueError:
    print("invalid")

