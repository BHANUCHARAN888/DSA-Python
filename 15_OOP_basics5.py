# Abstraction method
# Hiding the complex internal details and showing the essential details
# Syntax of Abstraction method
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Barks")
class Cat(Animal):
    def make_sound(self):
        print("Meoms")
d=Dog()
d.make_sound()
c=Cat()
c.make_sound()
print("--------------------------------------------")
# Examples:-
# 1
from abc import ABC, abstractmethod
class Paymentmethod(ABC):
    @abstractmethod
    def process_payment(amount):
        pass
class CreditcardPayment(Paymentmethod):
    def process_payment(self, amount):
        print(f"Paid Rs.{amount}/- through Credit card")
class UpiPayment(Paymentmethod):
    def process_payment(self, amount):
        print(f"Paid Rs.{amount}/- through UPI")
cc=CreditcardPayment()
cc.process_payment(5000)
u=UpiPayment()
u.process_payment(5000)
print("--------------------------------------------")
# 2
from abc import ABC,abstractmethod
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class Laptop(Device):
    def turn_on(self):
        print("Laptop is now ON")
class Smartphone(Device):
    def turn_on(self):
        print("Smartphone is now ON")
l=Laptop()
l.turn_on()
s=Smartphone()
s.turn_on()
print("--------------------------------------------")
# 3
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        area = self.length * self.width
        return print(f"Area of rectangle is {area}sq.m")
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        area = 3.14 * self.radius * self.radius
        return print(f"Area of circle is {area}sq.m")
c=Rectangle(20,40)
c.area()
c=Circle(40)
c.area()
print("--------------------------------------------")
# 4
from abc import ABC, abstractmethod
class MessageService(ABC):
    def __init__(self, to, content):
        self.to=to
        self.content=content
    @abstractmethod
    def send_message(self):
        pass
class EmailService(MessageService):
    def send_message(self):
       return  print(f"Sending Email to:-{self.to}: {self.content}")
class SMSservice(MessageService):
    def send_message(self):
        return print(f"Sending SMS to:-{self.to}: {self.content}")
c=EmailService("Chaarz@123.com","Hello this text from Email")
c.send_message()
c=SMSservice(9494949494,"Hello this text from SMS service")
c.send_message()
print("--------------------------------------------")
# 5
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, holder_name, balance):
        self.holder_name=holder_name
        self.balance=balance
    def info(self):
        print(f"Name: {self.holder_name}")
        print(f"Balance: {self.balance}")
    @abstractmethod
    def withdraw(self,amount):
        pass
    def get_balance(self):
        return print(f"Current balance:{self.balance}")
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance >= amount:
         self.balance -= amount
         return print(f"With-drew: Rs.{amount}, New-Balance: {self.balance}")
        else:
            return print("In-sufficient balance")
c=SavingsAccount("Bhanu",30000)
c.info()
c.withdraw(5000)
c.get_balance()
print("--------------------------------------------")
# 6
from abc import ABC, abstractmethod
class MediaFiles(ABC):
    def __init__(self, filename):
        self.filename=filename
    @abstractmethod
    def play(self):
        pass
class Audiofile(MediaFiles):
    def play(self):
        return print(f"Playing audio file:{self.filename}")
class Videofile(MediaFiles):
    def play(self):
        return print(f"Playing video file:{self.filename}")
c=Audiofile("PagalWorld.mp3")
c.play()
c=Videofile("Movies.mp4")
c.play()
print("--------------------------------------------")
# 7
from abc import ABC, abstractmethod
class Course(ABC):
    def __init__(self, title, instructor):
        self.title=title
        self.instructor=instructor
    @abstractmethod
    def start_course(self):
        pass
class PythonCourse(Course):
    def start_course(self):
        return print(f"Starting Python course: {self.title} by {self.instructor}")
class WebDevCourse(Course):
    def start_course(self):
        return print(f"Starting Web Development course: {self.title} by {self.instructor}")
c=PythonCourse("Python for Beginners","Bhanu")
c.start_course()
c=WebDevCourse("Full-stack Web-Dev","Charan")
c.start_course()
print("--------------------------------------------")
# 8
from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__(self,mode):
        self.mode=mode
    @abstractmethod
    def travel(destination):
        pass
class Car(Transport):
    def travel(self,destination):
        return print(f"Traveling to {destination} from Vizag by car.")
class Train(Transport):
    def travel(self,destination):
        return print(f"Travelling to {destination} from Kharagpur by train.")
c=Car("road")
c.travel("Hyderabad")
t=Train("track")
t.travel("Vizag")
print("--------------------------------------------")
# 9
from abc import ABC, abstractmethod
class Notification(ABC):
    def __init__(self,sender):
        self.sender=sender
    @abstractmethod
    def send(self,message,receiver):
        pass
class EmailNotification(Notification):
    def send(self,message,receiver):  
        return print(f"Email from {self.sender} to {receiver}: {message}")
class SMSNotification(Notification):
    def send(self,message,receiver):
        return print(f"SMS from {self.sender} to {receiver}: {message}")
e=EmailNotification("charan@123.com")
e.send("This message is from Email","bhanu@123.com")
s=SMSNotification("949493")
s.send("This message is from SMS","949494")
print("--------------------------------------------")
# 10
from abc import ABC,abstractmethod
class PaymentGateWay(ABC):
    def __init__(self, sender, receiver, amount):
        self.sender=sender
        self.receiver=receiver
        self.amount=amount
    @abstractmethod
    def process_payment(self):
        pass
    def info(self):
        print(f"Sender: {self.sender}")
        print(f"Receiver: {self.receiver}")
        print(f"Amount: {self.amount}")
class UPIPayment(PaymentGateWay):
    def __init__(self, sender, receiver, amount, upi_id):
        super().__init__(sender,receiver,amount)
        self.upi_id=upi_id
    def process_payment(self):
      if '@' in self.upi_id:
          print(f"UPI Payment is successful from {self.sender} to {self.receiver} of Rs.{self.amount} using {self.upi_id}")
      else:
          print("Invalid UPI ID!")
class CardPayment(PaymentGateWay):
    def __init__(self, sender, receiver, amount, card_number):
        super().__init__(sender,receiver,amount)
        self.card_number=card_number
    def process_payment(self):
      if len(self.card_number) == 16:
          print(f"credit-card Payment is successful from {self.sender} to {self.receiver} of Rs.{self.amount} using {self.card_number}")
      else:
          print("Invalid card!")
c=UPIPayment("Bhanu","Amazon",1500,"bhanu@123.ybl")
c.info()
c.process_payment()
c=CardPayment("Charan","Flipcark",1000,"1234567809876543")
c.info()
c.process_payment()
print("--------------------------------------------")
# 11
from abc import ABC,abstractmethod
class SmartDevice(ABC):
    def __init__(self,device_name):
        self.device_name=device_name
    @abstractmethod
    def turn_on(self):
        pass
    def turn_off(self):
        pass
    def status(self):
        print(f"Device: {self.device_name}")
class SmartLight(SmartDevice):
    def __init__(self, device_name, brighness):
        super().__init__(device_name)
        self.brightness=brighness
    def turn_on(self):
        print(f"{self.device_name} turned ON with brightness {self.brightness}")
    def turn_off(self):
        print(f"{self.device_name} is now OFF")
class SmartAC(SmartDevice):
    def __init__(self, device_name, temperature):
         super().__init__(device_name)
         self.temperature=temperature
    def turn_on(self):
      if self.temperature in range(16,30):
          print(f"{self.device_name} turned ON at temperature {self.temperature}")
      else:
          print("Invalid temperature setting!!")
    def turn_off(self):
        print(f"{self.device_name} is now OFF")
c=SmartLight("Living-Roon-Light",70)
c.turn_on()
c.turn_off()
c=SmartAC("A/C",26)  
c.turn_on()
c.turn_off() 
print("--------------------------------------------")
      
        


          
          


       
        

    


        
       
