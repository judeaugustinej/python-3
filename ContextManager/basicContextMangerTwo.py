"""
object can be accessed using 'as' keyword
__exit__() deleted the object created in __enter__().

"""
class InContext:

    def __init__(self,context):
        print("InContext.__init__({})".format(context))

    def foo(self):
        print('InContext.foo()')

    def __del__(self):
        print('I am dead')

class MyContext:

    def __init__(self):
        print("MyContext.__init__()")

    def __enter__(self):
        print("MyContext.__enter__")
        return InContext(self)

    def __exit__(self,exc_type,exc_val,exc_tb):
        print("MyContext.__exit__()")


if __name__ == "__main__":
    with MyContext() as c:
        print("c is {} and type of {} ".format(c,type(c)))
#Output
"""
MyContext.__init__()
MyContext.__enter__
InContext.__init__(<__main__.MyContext object at 0x2ae1251eca20>)
c is <__main__.InContext object at 0x2ae1251ecb70> and type of <class '__main__.InContext'>
MyContext.__exit__()
I am dead

"""
