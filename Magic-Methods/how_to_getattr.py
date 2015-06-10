""" __getattr__(self,name) 
This method only gets called when a nonexistent attribute is accessed.
This can be useful for catching and redirecting common misspellings,
giving warnings about using deprecated attributes.
"""

#Without Subclassing __getattr__()
class A(object):
  def __init__(self):
    self.a = 42


if __name__ == "__main__":

  obj = A()
  print(obj.x)
#---Output---
"""
-sh-3.2$ python3 without_getattr.py
Traceback (most recent call last):
  File "without_getattr.py", line 9, in <module>
    print(obj.x)
AttributeError: 'A' object has no attribute 'x'

"""

#With __getattr__()
class A(object):
  def __init__(self):
    self.a = 42

  def __getattr__(self, attr):
    if attr in ["b", "c"]:
      return 42
    raise AttributeError("%r object has no attribute %r" %
                         (self.__class__, attr))


if __name__ == "__main__":

  a =A()
  print(a.a)
  print(a.x)

#---Output---
"""
-sh-3.2$ python3 myget1.py
42
Traceback (most recent call last):
  File "myget1.py", line 16, in <module>
    print(a.x)
  File "myget1.py", line 9, in __getattr__
    (self.__class__, attr))
AttributeError: <class '__main__.A'> object has no attribute 'x'

"""

#use the dict's key with MyClass instance to access the dict

class MyClass(object):
  def __init__(self):
    self.data = {'a': 'v1', 'b': 'v2'}
    
  def __getattr__(self, attr):
    return self.data[attr]
    
if __name__ == "__main__":

  obj = MyClass()
  print(obj.a)  #'v1'
  print(obj.b)  #'v2'
  
  
        
        
        
