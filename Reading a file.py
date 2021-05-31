'''employee_file = open("calculator.py","w")
print(employee_file.readable())

employee_file.close()'''
#use "a"for append informatin to the end of file and use "w" to wrie or change/
#modfy anf "r+" is used to both read and write.

'''employee_file = open("calculator.py","r")
print(employee_file.readable())

employee_file.close()'''

'''employee_file = open("dictionary.py","r")
print(employee_file.read())

employee_file.close()'''

'''employee_file = open("dictionary.py","r")
print(employee_file.readline())employee_file = open("dictionary.py","r")
print(employee_file.read())

employee_file.close(
print(employee_file.readline())
employee_file.close()'''

'''employee_file = open("dictionary.py","r")
print(employee_file.readlines())
#it gives each lines as a list of lines seperated by commas
employee_file.close()'''

employee_file = open("dictionary.py","r")
print(employee_file.readlines()[2])
#it specify the line to which is printed with index.
employee_file.close()
