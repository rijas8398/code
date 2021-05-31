'''
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self,x,y):

        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y


p = Point(7,6)
print(p.getx())
print(p.gety())

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(7,6)
print(p.distanceFromOrigin())

???Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. Create an instance method called limbs that, when called,
returns the total number of limbs the animal has. To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. Call the limbs method on the spider instance and save the
result to the variable name spidlimbs.

class Animal:
    def __init__(self,arms,legs):
        self.x=arms
        self.y=legs

    def limbs(self):
        return (self.x+self.y)

spider=Animal(4,4)
spidlimbs=spider.limbs()
print(spidlimbs)


Here is a simple function called distance involving our new Point objects. The job of this function is to figure out the distance between two points.

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

def distance(point1, point2):
    xdiff = point2.getx()-point1.getx()
    ydiff = point2.gety()-point1.gety()


    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4,3)
q = Point(0,0)
print(distance(p,q))

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

p = Point(7,6)
print(p)
print(p.distanceFromOrigin())

Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables in the constructor: name, brand, and fiber. When an instance of Cereal is
printed, the user should see the following: “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!” To the variable name c1, assign an instance of Cereal whose
name is "Corn Flakes", brand is "Kellogg's", and fiber is 2. To the variable name c2, assign an instance of Cereal whose name is "Honey Nut Cheerios", brand is "General Mills", and fiber is 3.
Practice printing both!

class Cereal:
    def __init__(self,n,b,f):
        self.name=n
        self.brand=b
        self.fiber=f

    def __str__(self):
        return "{} is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.fiber)
c1=Cereal('Corn Flakes',"Kellogg's",2)
c2=Cereal("Honey Nut Cheerios","General Mills",3)
print(c1)
print(c2)

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distanceFromOriginy(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return '{},{}'.format(self.x,self.y)

    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

def distance(point1, point2):
    xdiff = point2.getx()-point1.getx()
    ydiff = point2.gety()-point1.gety()


    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist


p = Point(4,3)
q = Point(5,9)
print(p+q)
print(p-q)


L = ["Cherry", "Apple", "Blueberry"]

print(sorted(L, key=len))
#alternative form using lambda, if you find that easier to understand
print(sorted(L, key= lambda x: len(x)))

class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)


class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)





