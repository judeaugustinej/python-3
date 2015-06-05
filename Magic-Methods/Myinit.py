"""
__init__() takes object as the first argument.
It is uset to initailze the object.
"""
class Foo(object):
    
    def __init__(self):
        print(self)
        
a = Foo()
#<__main__.Foo object at 0x02C4E8D0>
print(a)
#<__main__.Foo object at 0x02C4E8D0>


class Init(object):

    def __init__(self,*args):

        print(self,*args)

objNew = Init(5,6)    #<__main__.Init object at 0x02E5E970> 5 6



