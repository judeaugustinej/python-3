"""Descriptor Protocol.
   Any class with __get__,__set__/__delete__ method is called a descriptor
   Descriptor are applied on class attributes and not on instance variables.
   
"""

class ValueDescriptor:

    def __init__(self,name):

        self.name = name

    def __get__(self,instance,owner):

        return instance.__dict__[self.name]

    def __set__(self,instance,value):

        if value >= 0:

            instance.__dict__[self.name] = value
        else:
            raise ValueError("what is wrong with you")
    def __delete__(self,instance): 
        
        raise NotImplementedError("Cannot Delete attributes")
    

class MyShop:

    weight = ValueDescriptor("weight")
    price  = ValueDescriptor("price")

    def __init__(self,description,weight,price):

        self.description = description
        self.weight = weight
        self.price = price

    def sub_total(self):

        return self.weight * self.price


if __name__ == "__main__":

    rice = MyShop('rice packet',50,100)
    rice.weight = 40
    print(rice.weight)

    oops = [rice,MyShop,ValueDescriptor]

    for element in oops:
        print(element)
        for key,value in element.__dict__.items():
            print(str(key)+"----->"+str(value))
        print(" ")
#---Output---
"""
40
<__main__.MyShop object at 0x2b1d3662ab38>
weight----->40
description----->rice packet
price----->100

<class '__main__.MyShop'>
sub_total-----><function MyShop.sub_total at 0x2b1d365f0c80>
__doc__----->None
__module__----->__main__
weight-----><__main__.ValueDescriptor object at 0x2b1d3662aac8>
__init__-----><function MyShop.__init__ at 0x2b1d365f0bf8>
price-----><__main__.ValueDescriptor object at 0x2b1d3662ab00>
__dict__-----><attribute '__dict__' of 'MyShop' objects>
__weakref__-----><attribute '__weakref__' of 'MyShop' objects>

<class '__main__.ValueDescriptor'>
__get__-----><function ValueDescriptor.__get__ at 0x2b1d365f0a60>
__set__-----><function ValueDescriptor.__set__ at 0x2b1d365f0ae8>
__init__-----><function ValueDescriptor.__init__ at 0x2b1d365f09d8>
__doc__----->None
__module__----->__main__
__delete__-----><function ValueDescriptor.__delete__ at 0x2b1d365f0b70>
__weakref__-----><attribute '__weakref__' of 'ValueDescriptor' objects>
__dict__-----><attribute '__dict__' of 'ValueDescriptor' objects>

"""
