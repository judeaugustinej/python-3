class InContext:

    def __init__(self,context):
        print("InContext.__init__({})".format(context))
        print(" ")

    def foo(self):
        print('InContext.foo()')
        print(" ")

    def __del__(self):
        print('I am dead')
        print(" ")

class MyContext:

    def __init__(self):
        print("MyContext.__init__()")
        print(" ")

    def __enter__(self):
        print("MyContext.__enter__")
        y =  InContext(self)
        print("{} {}".format(y,type(y)))
        print(" ")
        print("I am back")
        return y
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("MyContext.__exit__()")
        print(" ")

if __name__ == "__main__":
    with MyContext() as c:
        print("{} {}".format(c,type(c)))

"""
[sunkaray@SUT-LNX-1 contextManger]$ python3 basicContextTwoC.py
MyContext.__init__()

MyContext.__enter__
InContext.__init__(<__main__.MyContext object at 0x2ad6a39a2a58>)

<__main__.InContext object at 0x2ad6a39a2ba8> <class '__main__.InContext'>

I am back
<__main__.InContext object at 0x2ad6a39a2ba8> <class '__main__.InContext'>
MyContext.__exit__()

I am dead


"""
