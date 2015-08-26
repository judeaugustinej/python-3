""""
context manager are enable by using the keywork 'with'

__enter__() is excecuted when the code within the context and

__exit__() is run when the execution leaves the 'with' block
""""
class MyContext:

    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("In the context__enter__")

    def __exit__(self,exc_type,exc_val,exc_tb):
        print("__exit__()")

if __name__ == "__main__":
    with MyContext():
        print("What is context manager")

# Output
"""
[sunkaray@SUT-LNX-1 contextManger]$ python3 basicContext.py
__init__
In the context__enter__
What is context manager
__exit__()
[sunkaray@SUT-LNX-1 contextManger]$

"""
