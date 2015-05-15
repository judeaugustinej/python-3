"""
__init__() takes object as the first argument.
It is uset to initailze the object.
"""

class Init(object):

    def __init__(self,*args):

        print(self,*args)

objNew = Init(5,6)    #<__main__.Init object at 0x02E5E970> 5 6
