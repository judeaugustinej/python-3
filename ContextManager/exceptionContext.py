from contextlib import contextmanager

@contextmanager
def exceptionHandler():
    try:
        yield
    except :
        raise


def myDivide(a,b):
    with exceptionHandler():
        y = a/b
        return y

def mySquare(num):
    with exceptionHandler():
        return num ** 2
"""
def myDivide(a,b):
    try:
        y = a/b
    except :
        raise
    else:
        return y
"""
if __name__ == "__main__":
    print(myDivide(1,1))
    print(mySquare("10"))
