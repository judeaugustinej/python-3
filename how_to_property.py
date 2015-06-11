"""Few example on @property"""

#property to used to compute attribute on demand.

import math

class Circle:

 def __init__(self,radius):
  self.radius = radius

 @property
 def area(self):
  return math.pi*self.radius

 @property
 def perimeter(self):
  return 2*math.pi*self.radius
  
class Person(object):

 def __init__(self,name,age):
  self.name = name
  self.age  = age

 @property
 #Make name a property.
 def name(self):
  return self._name

 @name.setter
 #This method is called whenever self.name is accessed
 def name(self,value):
  if not isinstance(value,str):
   raise TypeError("Your name Please !")
  self._name = value

 @name.deleter
 def name(self):
  raise AttributeError("What is wrong with your Name")

 @property
 def age(self):
  return self._age

 @age.setter
 def age(self,value):
  if value > 18:
   self._age = value
  else:
   raise ValueError("You cannot vote")

 @age.deleter
 def age(self):
  raise AttributeError("Please don't do that")


if __name__ == "__main__":

 c = Circle(4)
 print("""For a circle of radius {}
the area is {}
and perimeter is {}
""".format(c.radius,c.area,c.perimeter))

#--Output--
"""
-sh-3.2$ python3 je1.py
For a circle of radius 4
the area is 12.566370614359172
and perimeter is 25.132741228718345

"""
 person = Person("Jude",25)
 
