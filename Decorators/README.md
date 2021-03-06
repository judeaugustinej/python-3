###Decorators
#####Function is an object in PYTHON
``` python

def foo():
  print("fooooo")
  
if __name__ == "__main__":
    y = foo
    print(y)

    y()

```
Output
```
>>> 
<function foo at 0x02EF9F18>
fooooo
>>> 
```
###Basic Decorator
```
def outerFoo(f):
    def inner():
        return f() + " and Just got decorated"
    return inner

@outerFoo
def foo():
    return "I am foo()"

if __name__ == "__main__":
    print(" decoration")
    print(foo())


```
####Output
```
[sunkaray@SUT-LNX-1 decorators]$ python3 decoratorBasic.py
 decoration
I am foo() and Just got decorated

```

#####Closure Basic
```
def outerFoo(num):
    x = num
    def innerFoo():
        print("The number is {}".format(x))
    return innerFoo

if __name__ == "__main__":
    outer1 = outerFoo(1)
    outer1()

    outer2 = outerFoo(2)
    outer2()

```
##### Output
```
[sunkaray@SUT-LNX-1 decorators]$ python3 closureBasic.py
The number is 1
The number is 2
[sunkaray@SUT-LNX-1 decorators]$

```
##### Class Decorators without args
```
class DecoratorsNoArgs:

    def __init__(self,f):
        print("In __init__()")
        self.f = f

    def __call__(self,*args):
        print("In __call__")
        self.f(*args)
        print("leaving __call__")


@DecoratorsNoArgs
def sayFoo(name):
    print("Hi {}".format(name))

if __name__ == "__main__":
    sayFoo('jude')


```
###Output
```
In __init__()
In __call__
Hi jude
leaving __call__


```
