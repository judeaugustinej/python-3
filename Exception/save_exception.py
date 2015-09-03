"""
We handle the exception ie using sys module,
we extract the exception type,value and traceback object.
Using the traceback  object we print out the traceback itself.
"""
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
