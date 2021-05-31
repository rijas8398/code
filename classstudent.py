'''other than datatypes like strings,numbers and boolean it can be create other datatypes
like student,computer etc is called as "class".
eg: class student
    basically defines the overview of student datatype.
    here use student as an object.we can use this class in other files also.'''

class student :
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
