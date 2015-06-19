#All about list and list comprehensions
>>>
>>> # list of cubes from number 0 to 9
>>> a = [ x**3 for x in range(10)]
>>> a
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>>
>>>
>>> #cubes of multiples of numbers below 9
>>> a = [ x**3 for x in range(10) if x%3==0]
>>> a
[0, 27, 216, 729]
>>> 
>>>
"""
The matching performed by fnmatch sits somewhere between the functionality of simple
string methods and the full power of regular expressions.
"""
>>> from fnmatch import fnmatch,fnmatchcase
>>>
>>> email_ids = [jude@Tcs.com,jude@apple.com,jude@nokia.com,james@tcs.com,john@apple.com,john@nokia.com]
>>> 
>>> tcs_email_id = [ email for email in email_ids if fnmatch(email,'*@tcs.com')]
>>> 
>>> tcs_email_id
['jude@Tcs.com', 'james@tcs.com']
>>> 
>>> #but for exact match
>>>
>>> tcs_email_id = [ email for email in email_ids if fnmatchcase(email,'*@tcs.com')]
>>> tcs_email_id
['james@tcs.com']
>>> 
#--what is any --?
"""
any(iterable)
Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
"""

>>> import os
>>> os.getcwd()
'C:\\Python34\\Lib'
>>> os.chdir('..')
>>> os.getcwd()
'C:\\Python34'
>>> 
