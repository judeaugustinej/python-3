
"""
__new__() takes the class as the first argument.
It is used to create the object.
"""

class New(object):

    def __new__(cls,*args):

        print(cls,*args)

objNew = New(5,6)  #<class '__main__.New'> 5 6
