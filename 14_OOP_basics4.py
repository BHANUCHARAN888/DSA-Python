# Polymorphism
# It alloys the object of different class into the same class.
# There are three types of polymorphism-Duck_typing, Operator_overloading, Method_overriding.

# Duck_typing:
# Examples
# 1
class Animal:
    def sound(self):
        print("Animal sounds")
class Duck:
    def sound(self):
        print("Duck quacks")
def frequency(hears):
    hears.sound()
c=Animal()
frequency(c)
c=Duck()
frequency(c)
print("-------------------------------------------------------")
# 2
class Animal:
    def sound(self):
        print("Animal sounds")
class Dog:
    def sound(self):
        print("Dog barks")
def frequency(hears):
    hears.sound()
c=Animal()
frequency(c)
c=Dog()
frequency(c)
print("-------------------------------------------------------")
# 3
class Car:
    def start_engine(self):
        print("Car engine start's")
class Bike:
    def start_engine(self):
        print("Bike engine start's")
def vehicle_start(v):
    v.start_engine()
c=Car()
vehicle_start(c)
c=Bike()
vehicle_start(c)
print("-------------------------------------------------------")
# 4
class Spotify:
    def play_song(self):
        print("Playing song from Spotify")
class YouTubemusic:
    def play_song(self):
        print("Playing song from YouTubeMusic")
def start_music(app):
    app.play_song()
c=Spotify()
start_music(c)
c=YouTubemusic()
start_music(c)
print("-------------------------------------------------------")
# 5
class GooglePay:
    def pay(self):
        print("Paid $500 from GooglePay")
class Phonepe:
    def pay(self):
        print("Paid $500 form Phonepe")
def make_payment(app):
    app.pay()
c=GooglePay()
make_payment(c)
c=Phonepe()
make_payment(c)
print("-------------------------------------------------------")
# 6
class ISRO:
    def launch_rocket(self):
        print("ISRO rocket launched successfully")
class NASA:
    def launch_rocket(self):
        print("NASA rocket launched with spaceX booster")
def start_mission(space_agency):
    space_agency.launch_rocket()
c=ISRO()
start_mission(c)
c=NASA()
start_mission(c)
print("-------------------------------------------------------")

# Operator overloading:
# + -> __add__    ,  * -> __mul__
# - -> __sub__    ,  / -> __truediv__
# == -> __eq__    ,  > or < -> __gt__
# Examples
# 1
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages + other.pages
b1=Book(100)
b2=Book(100)
print(f"{b1 + b2}pages")
# 2
class Box:
    def __init__(self, weight1):
        self.weight1=weight1
    def __add__(self,weight2):
        return self.weight1 + weight2.weight1
b1=Box(1000)
b2=Box(1000)
print(f"{b1+b2}kgs")
# 3
class Book:
    def __init__(self,pages_book1):
        self.pages_book1=pages_book1
    def __eq__(self, pages_book2):
        return self.pages_book1 == pages_book2.pages_book1
b1=Book(100)
b2=Book(101)
print(b1==b2)
# 4
class car:
    def __init__(self, speed1):
        self.speed1=speed1
    def __gt__(self,speed2):
        return self.speed1 > speed2.speed1
s1=car(125)
s2=car(145)
print(s1 > s2)
s1=car(145)
s2=car(125)
print(s1 > s2)
# 5
class CartItem:
    def __init__(self, price, quantity):
        self.price=price
        self.quantity=quantity
    def __add__(self, other):
       return (self.price * self.quantity) + (other.price * other.quantity)
Item1=CartItem(1000,2)
Item2=CartItem(2000,2)
print(Item1 + Item2)
# 6
class calculator:
    def __init__(self, operand1):
        self.operand1=operand1
    def __add__(self,operand2):
        return self.operand1 + operand2.operand1
    def __sub__(self, operand2):
        return self.operand1 - operand2.operand1
    def __mul__(self, operand2):
        return self.operand1 * operand2.operand1
    def __truediv__(self, operand2):
        return self.operand1 / operand2.operand1
Item1=calculator(10)
Item2=calculator(20)
print(Item1 + Item2)
print(Item1 - Item2)
print(Item1 * Item2)
print(Item1 / Item2)
print("-------------------------------------------------------")

# Method overriding 
# Implementing the method of class which is previously given to parent class
# Example
# 1
class Animal:
    def speak(self):
        print("Animal sounds")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
d=Dog()
a=Animal()
d.speak()
a.speak()
# 2(super method)
class Animal:
    def speak(self):
        print("Animal sounds")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")
c=Dog()
c.speak()
print("-------------------------------------------------------")
