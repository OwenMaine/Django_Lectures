class Dog():

    def __init__(self,breed,name):
        self.breed= breed
        self.name= name


mydog= Dog(breed= 'lab', name='sammy')
print(mydog.breed)
print(mydog.name)


class Circle():

    pi=3.14

    def __init__(self,radius=1):
        self.radius= radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius= new_r



myc =Circle(3)
print(myc.radius)
myc.set_radius(100)
print(myc.area())


class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("eating")

class Goat(Animal):

    def __init__(self):
        print("Goat created")

myd= Goat()
myd.whoAmI()
myd.eat()


class Book():

    def __init__(self,Author,Title,Pages):
        self.Author= Author
        self.Title= Title
        self.Pages= Pages

    def __str__(self):
        return "Author: {}, Title: {}, Pages: {}".format(self.Author,self.Title,self.Pages)

myb= Book("Jose", "Macbeth", "43")
print(myb)
