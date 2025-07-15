# OOPs means object oriented programming
# it is reusable and scalable
# using code as class(which is blue-print) and object(actual instance)

# Class and Object model
# Examples
class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
            return f"{self.brand} of {self.model} model in the Year {self.year}"
d=car("BMW", "X7", 2024)
print(d.display())

class bag:
     def __init__(self,brand,year):
          self.brand=brand
          self.year=year
     def display(self):
          return f"{self.brand} are easy to carry,manufactured in {self.year}"
d=bag("Nike",2020)
print(d.display())

class phone:
     def __init__(self,brand,model,year):
          self.brand=brand
          self.model=model
          self.year=year
     def display(self):
           return f"{self.brand} of {self.model} model is launched in the year {self.year}"
d=phone("Apple", "iPhone 16e", 2025)
print(d.display())

class TV:
     def __init__(self,brand,place,year):
          self.brand=brand
          self.place=place
          self.year=year
     def display(self):
          return f"{self.brand} brand is established in {self.place} in the year {self.year}"
d=TV("Sony","Japan",1946)
print(d.display())

class greeting:
     def __init__(self,name):
          self.name=name
     def description(self):
          return f"Happy Birthday {self.name}..."
g=greeting("Prabhas")
print(g.description())

class think:
     def __init__(self,sen):
          self.sen=sen
     def desc(self):
          return f"{self.sen} Bhanu!!"
t=think("Are you in the correct path")
print(t.desc())

     

