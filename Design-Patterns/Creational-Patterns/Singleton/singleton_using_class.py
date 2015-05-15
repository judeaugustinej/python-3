"""
__new__() takes the class as the first argument.
It is used to create the object.

__init__() takes object as the first argument.
It is uset to initailze the object.
"""
class Singleton:

    _instance = None 

    def __new__(cls,*args,**kwargs):

        if not cls._instance:

            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,*args,**kwargs):

        self.objList = args
        self.objDict = kwargs

        print(self.objList,self.objDict)

if __name__ == "__main__":

    y = Singleton([2,3,43],2)  #([2, 3, 43], 2) {}
    print(y)                   #<__main__.Singleton object at 0x03518830>

    p = Singleton('what','where') #('what', 'where') {}
    print(p)                      #<__main__.Singleton object at 0x03518830>
        

