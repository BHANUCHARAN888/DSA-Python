# Constructor method __init__()
class student:        #class block
      def __init__(self,name,age):  #constructor 
        self.name=name
        self.age=age
      def display(self):
        return f"My name is {self.name} and my age is {self.age}"

s=student("bhanu",18)  #object block
print(s.display())

# Example1
class Employee:
     def __init__(self,name,id,department): #constructor
      self.name=name
      self.id=id
      self.department=department
     def show_info(self):
        return f"Name: {self.name}, ID: {self.id}, Department: {self.department}"
E1=Employee("Bhanu",902719,'Frontend')       #object

print(E1.show_info())
E2=Employee("Anil",902720,'Backend')
print(E2.show_info())

# Example2
class Bank_account:
   def __init__(self,name,balance):
      self.name=name
      self.balance=balance
   def deposit(self,amount):
      self.balance+=amount
      print(f"Deposited amount: {amount}, New_balance: {self.balance}")
   def with_draw(self,amount):
      self.balance-=amount
      print(f"With_draw amount: {amount}, New_balance: {self.balance}")
   def show_balance(self):
      print(f"Account_holder: {self.name}, Balance: {self.balance}")

s1=Bank_account("Bhanu",10000)
s1.show_balance()
s1.deposit(3000)
s1.with_draw(2000)

# Example3
class calculator:
   def __init__(self,num1,num2):
      self.num1=num1
      self.num2=num2
   def add(self):
      result = self.num1 + self.num2
      print(f"sum of {self.num1} and {self.num2} is {result}")
   def sub(self):
      result = self.num1 - self.num2
      print(f"difference of {self.num1} and {self.num2} is {result}")
   def multi(self):
      result = self.num1 * self.num2
      print(f"product of {self.num1} and {self.num2} is {result}")
   def div(self):
      result = self.num1 / self.num2
      print(f"division of {self.num1} and {self.num2} is {result}")
   def display_num(self):
      print(f"num1: {self.num1} and num2: {self.num2}")
c=calculator(5,5)
c.display_num()
c.add()
c.sub()
c.multi()
c.div()

# Example4
class rectangle:
   def __init__(self,length,bredth):
      self.length=length
      self.bredth=bredth
   def area_R(self):
      result = self.length * self.bredth
      print(f"Area of Rectangle: {result}")
   def perimeter_R(self):
      result = 2 * (self.length + self.bredth)
      print(f"Perimeter of Rectangle: {result}")
   def display_parameter(self):
      print(f"Length:{self.length}, Bredth:{self.bredth}")
r=rectangle(7,5)
r.display_parameter()
r.area_R()
r.perimeter_R()

# Example5
class studentMarks:
   def __init__(self,name,roll_num,maths_marks,physics_marks,chemistry_marks):
      self.name=name
      self.roll_num=roll_num
      self.maths_marks=maths_marks
      self.physics_marks=physics_marks
      self.chemistry_marks=chemistry_marks
   def total_marks(self):
       total = self.maths_marks + self.physics_marks + self.chemistry_marks
       print(f"Total sum of all the subject marks: {total}")
   def average_marks(self):
       Average = (self.maths_marks + self.physics_marks + self.chemistry_marks)/3
       print(f"Average of three subjects:{Average}")
   def display_info(self):
      print(f"Name: {self.name}, Roll.no.: {self.roll_num}, Maths: {self.maths_marks}, Physics: {self.physics_marks}, Chemistry: {self.chemistry_marks}")  
d=studentMarks("Bhanu",20,90,80,90)
d.display_info()
d.total_marks()
d.average_marks()