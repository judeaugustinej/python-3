###Storing exception traceback
```
try:

    a = 1/0

except Exception,e:

    exc_tuple = sys.exc_info()
```

> Now If we print the tuple the values will be this.

1. exc_tuple[0] value will be "ZeroDivisionError"
2. exc_tuple[1] value will be "integer division or modulo by zero" (String passed as parameter to the exception class)
3. exc_tuple[2] value will be "trackback object at (some memory address)"

> The above details can also be fetched by simply printing the exception in string format.
```
print(e)
```

> Going a step further
```
import sys
import traceback

try:
    a = 1/0
except Exception as e:

    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(exc_value.__doc__)
    print(exc_value)
    print(exc_traceback)
    traceback.print_tb(exc_traceback, limit=1)
    print(exc_type.__name__)
    print("-------------------------")
    raise
```

####Output
```
>>> 
Second argument to a division or modulo operation was zero.
division by zero
<traceback object at 0x03250148>
  File "//10.166.0.56/chn-project/VDIFoldered/judeaugustine.j/Desktop/decorators/save_exception.py", line 5, in <module>
    a = 1/0
ZeroDivisionError
-------------------------
Traceback (most recent call last):
  File "//10.166.0.56/chn-project/VDIFoldered/judeaugustine.j/Desktop/decorators/save_exception.py", line 5, in <module>
    a = 1/0
ZeroDivisionError: division by zero
>>> 
```
