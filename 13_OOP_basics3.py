# Inheritance-the way of reusability code of existing classes
# example-children are inherit traits of parents
# Inheritance model
# Example
class Parent:
    def display(self):
        print("This is parent class")
class child(Parent):
    def show(self):
        print("This is child class")
c=child()
c.show()
c.display()
print("---------------------------------------------------------------")

# Example1
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class employee(person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary=salary
    def show_employee(self):
        print(f"Salary: {self.salary}")
c=employee('Bhanu',20,50000)
c.show_details()
c.show_employee()
print("---------------------------------------------------------------")


# Example2
class vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
class car(vehicle):
    def __init__(self, brand, model, price):
        super().__init__(brand, model)
        self.price=price
    def car_info(self):
        print(f"Price: {self.price}")
c=car("TOYOTA","INNOVA-crista",2500000)
c.info()
c.car_info()
print("---------------------------------------------------------------")

# Example3
# Multi-level inheritance
# Using the attributes of parent in child classes multiple times is call multi-level inheritance
class person:
    def __init__(self, name, age, place):
        self.name=name
        self.age=age
        self.place=place
    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Place: {self.place}')
class student(person):
    def std(self):
        print(f"{self.name} is student")
class academic_student(student):
    def acade_std(self):
        print(f"{self.name} is studying at IIT")
c=academic_student("Bhanu",20,"Vizag")
c.info()
c.std()
c.acade_std()
print("---------------------------------------------------------------")

# Example4
# Multiple inhertance
# Using more than one parent class in child class is called as multiple inheritance
# 1
class father:
    def f_info(self):                                                           
        print("The skills of father is working,earning,protecting")
class mother:
    def m_info(self):
        print("The skills of mother is cooking,caring,protecting")
class Child(father,mother):
    def c_info(self):
        print("The skills of children is playing,studying,annoying")
c=Child()
c.f_info()
c.m_info()
c.c_info()
print("---------------------------------------------------------------")

# 2
class Laptop:                              #parent-class1
    def __init__(self,brand,RAM):
        self.brand=brand
        self.RAM=RAM
    def laptop_specs(self):
        print(f"Laptop-brand: {self.brand}")
        print(f"RAM: {self.RAM}")
class Student:                             #parent-class2
    def __init__(self,name,college):
        self.name=name
        self.college=college
    def student_info(self):
        print(f"Name: {self.name}")
        print(f"College: {self.college}")
class Coder(Laptop,Student):               #child-class(with both parent classes)
    def __init__(self, brand, RAM, name, college):
        Laptop.__init__(self,brand,RAM)
        Student.__init__(self,name,college)              
    def daily_routine(self):
        print("Wakeup-code-debug-sleep-repeat")
c=Coder("HP","16GB","Bhanu","Aakash")      #object
c.laptop_specs()
c.student_info()
c.daily_routine()
print("---------------------------------------------------------------")

# 3
class Employee:                                                        #parent-class1
    def __init__(self, emp_id, name, department):
        self.emp_id=emp_id
        self.name=name
        self.department=department
    def emp_info(self):
        print(f"Employee-ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
class Device:                                                          #parent-class2
    def __init__(self, device_type, brand, OS):
        self.device_type=device_type
        self.brand=brand
        self.OS=OS
    def device_info(self):
        print(f"Device-name: {self.device_type}")
        print(f"Brand: {self.brand}")
        print(f"OS: {self.OS}")
class AccessSystem(Employee,Device):                                    #child-class(with both parent classes)
    def __init__(self, emp_id, name, department, device_type, brand, OS, access_level):
        Employee.__init__(self, emp_id, name, department)
        Device.__init__(self, device_type, brand, OS)
        self.access_level=access_level
    def show_access(self):
        print(f"Access-Level: {self.access_level}")
c=AccessSystem(456,"Bhanu","IT","Laptop",'HP',"Windows 11","Admin")     #object
c.emp_info()
c.device_info()
c.show_access()
print("---------------------------------------------------------------")

# Example5
# Hybrid inheritance
# combination of two or more inheritance is called Hybrid inheritance
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def P_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Employee(Person):
    def __init__(self, name, age, emp_id, department):
        Person.__init__(self, name, age)
        self.emp_id=emp_id
        self.department=department
    def Em_info(self):
        print(f"ID: {self.emp_id}")
        print(f"Department: {self.department}")
class Engineer(Person):
    def __init__(self, name, age, specialization):
        Person.__init__(self, name, age)
        self.specialization=specialization
    def En_info(self):
        print(f"Specialization: {self.specialization}")
class TechLead(Employee,Engineer):
    def __init__(self, name, age, emp_id, department, specialization, project_name):
        Employee.__init__(self, name, age, emp_id, department)
        Engineer.__init__(self, name, age, specialization)
        self.project_name=project_name
    def show_lead_info(self):
        print(f"Project_Name: {self.project_name}")
c=TechLead("Bhanu",20,456,"IT","AIML","nxt Gen-GPT")
c.P_info()
c.Em_info()
c.En_info()
c.show_lead_info()
print("---------------------------------------------------------------")

# Example6
# Hierarchical inheritance
# Multiple child classes inherit from same parent class
class Animal:
    def speak(self):
        print("Animals make sound")
class Cat(Animal):
    def meom(self):
        print("cat meoms")
class Dog(Animal):
    def bark(self):
        print("dog barks")
d=Dog()
d.speak()
d.bark()

c=Cat()
c.speak()
c.meom()
print("---------------------------------------------------------------")