""" __call__() allows instance of a class to be called like a function.
   It is useful if instance needs to change its state
"""

class Call(object):

    def __init__(self):

        print("In __init__")

    def __call__(self):
        print("In __call__")
        
class WhyCall(Call):
    
    def __init__(self,x,y):

        super().__init__()
        self.x, self.y = x, y
        
    def __call__(self,x,y):

        super().__call__()
        self.x, self.y = x,y

        
if __name__ == "__main__":

    objCall = Call()                                  #In __init__
    objCall()                                         #In __call__

    objWhyCall = WhyCall(4,5)                        
    print(objWhyCall.x,objWhyCall.y)                   #In __init__
                                                       #4 5

    objWhyCall(7,'*')
    print(objWhyCall.x,objWhyCall.y)                  #In __call__
                                                      #7 *
    
    



