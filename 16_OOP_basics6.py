# Encapsulation 
# means hiding the internal object and only allow access through function
# useful for increase security, protect data from unwanted access, make code more modular and readable
# Example
# 1
class BankAccount:
    def __init__(self, balance):
        self.balance=balance
    def deposit(self, amount):
        if amount>0 :
            self.balance+=amount
        else:
            print("Invalid deposit")
    def withdraw(self, amount):
        if 0<amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.balance
c=BankAccount(10000)
c.deposit(5000)
c.withdraw(2500)
print(c.get_balance())
print("---------------------------------------------------------")
# 2
class StudentRecord:
   def __init__(self):
       self.__name= ""
       self.__roll= ""
       self.__marks= {}
   def set_name(self, name):
           self.__name=name
   def get_name(self):
        return self.__name
   def set_roll(self, roll):
           self.__roll=roll
   def get_roll(self):
        return self.__roll
   def add_marks(self, subject, marks):
       if 0 <= marks <= 100:
        self.__marks[subject]=marks
       else:
        print(f"Invalid marks for {subject}")
   def get_marks(self):
        return self.__marks
   def get_t_marks(self):
        return sum(self.__marks.values())
   def avg(self):
       if self.__marks:
           return sum(self.__marks.values())/len(self.__marks)
       else:
           return 0
s1=StudentRecord()
s1.set_name("Bhanu")
s1.set_roll("24T91A4420")
s1.add_marks("Maths:",86)
s1.add_marks("Physics:",84)
s1.add_marks("Chemistry:",83)
print("Total marks:", s1.get_t_marks())
print("Average:", s1.avg())
print("---------------------------------------------------------")
# 3
class StudentProgress:
    def __init__(self):
        self.__name=""
        self.__roll=""
        self.__marks={}
        self.__attendance=""
        self.__status=""
    def set_details(self,name,roll):
        self.__name=name
        self.__roll=roll
    # def get_details(self):
    #     print(f"Name: {self.__name}")
    #     print(f"Roll.no.: {self.__roll}")
    def add_marks(self,subject,marks):
        if 0 <= marks <= 100:
         self.__marks[subject]=marks
        else:
            print("Invalid subject marks")
    def get_t_marks(self):
        return sum(self.__marks.values())
    def avg(self):
        return sum(self.__marks.values())/len(self.__marks)
    def set_attendance(self,attendance):
        if 0 <= attendance <=100:
            self.__attendance=attendance
        else:
            print("Invalid percentage")
    def get_status(self):
        avg=sum(self.__marks.values())/len(self.__marks)
        if  self.__attendance>=75 and avg >=40:
         print("status: PASS")
        else:
         print("status:Fail")
    def get_summary(self):
         return print(f"Name: {self.__name}\nRoll No.: {self.__roll}\nTotal Marks: {sum(self.__marks.values())}\nAverage Marks: {sum(self.__marks.values())/len(self.__marks)}\nAttendance: {self.__attendance}\n") 
s1=StudentProgress()
s1.set_details("Bhanu","24T91A4420")
s1.add_marks("Maths:",85)
s1.add_marks("Physics:",90)
s1.add_marks("Chemistry:",90)
s1.set_attendance(90)
print(s1.get_summary())
s1.get_status()
print("---------------------------------------------------------")
# 4
class Studentfee:
    def __init__(self):
        self.__name=""
        self.__roll=""
        self.__total_fee=0
        self.__paid_fee=0
        self.__balance=0
    def set_details(self, name, roll, total_fee):
        self.__name=name
        self.__roll=roll
        self.__total_fee=total_fee
        self.__paid_fee=0
        self.__balance=total_fee
    def pay_fee(self,amount):
        self.__amount=amount
        self.__balance = self.__total_fee - amount
        self.__paid_fee=amount
        if self.__paid_fee > self.__total_fee:
            print("Extra amount is detected!")
        else:
            return 0
    def get_summary(self):
        return print(f"Name: {self.__name}\nRoll.No.: {self.__roll}\nTotal fee: {self.__total_fee}\nPaid fee: {self.__amount}\nBalance: {self.__balance}\n")
    def check_clearance(self):
        if self.__balance==0:
            print("Fee Cleared")
        else:
            print("Fee pending")
s1=Studentfee()
s1.set_details("Bhanu","24T91A4420",100000)
s1.pay_fee(100000)
print(s1.get_summary())
s1.check_clearance()
print("---------------------------------------------------------")
# 5
class EmployeeSalary:
    def __init__(self):
        self.__name=""
        self.__emp_id=""
        self.__base_salary=""
        self.__bonus=0
        self.__deduction=0
        self.__net_salary=""
    def set_details(self, name, emp_id, base_salary):
        self.__name=name
        self.__emp_id=emp_id
        self.__base_salary=base_salary
    def add_bonus(self,amount):
        self.__bonus=amount+self.__bonus
        self.__net_salary=self.__base_salary+self.__bonus
    def apply_deduction(self,amount):
        self.__deduction=amount
        self.__net_salary=self.__net_salary-self.__deduction
        if self.__net_salary == 0:
            return print("Unable to deduct amount, balance is 0")
        else:
            return 0
    def get_summary(self):
        return print(f"Name: {self.__name}\nID: {self.__emp_id}\nBase Salary: {self.__base_salary}\nBonus: {self.__bonus}\nDeduction: {self.__deduction}\nNet Salary: {self.__net_salary}\n")
e1=EmployeeSalary()
e1.set_details("Bhanu","E4420",60000)
e1.add_bonus(10000)
e1.apply_deduction(20000)
print(e1.get_summary())

        


    
    

