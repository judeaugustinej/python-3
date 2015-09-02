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
