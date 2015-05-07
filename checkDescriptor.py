#checking the value before assigning using ValueDescriptor 
#An issue with NotImplemented execption in __delete__
#TypeError: exceptions must derive from BaseException
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
    def __delete__(self,instance): raise NotImplemented
    

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
    #Please read the output
    #del rice.weight
        
    
