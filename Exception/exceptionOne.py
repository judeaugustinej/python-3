def mySquare(num):
    try:
        return num ** 2
    except:
        raise
if __name__ == "__main__":
    print(mySquare(3))
    print("----------")
    print(mySquare('jude'))
    
#Output
"""
[sunkaray@SUT-LNX-1 jude]$ python3 exceptionOne.py
9
----------
Traceback (most recent call last):
  File "exceptionOne.py", line 10, in <module>
    print(mySquare('jude'))
  File "exceptionOne.py", line 3, in mySquare
    return num ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

"""
