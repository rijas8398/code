class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1=Employee('baby','salman',5001)
emp2=Employee('delli','vishnu',6001)

print(emp1.email)
print(emp2.fullname())
print(Employee.fullname(emp1))