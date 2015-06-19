#A gentle introduction into regular expression
#Regular expression are used  to filter texts or textstring.

"""
The special characters are:
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    
    {m,n}    Matches from m to n repetitions of the preceding RE.
    
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.

Note: A raw string is created by simply adding an ‘r’ character before the opening quote of a normal string.
When a string is raw, the python parser will not even attempt to make any substitutions within it

    Examples

        To find a 3 letter a character ending with  at ".at"
        r" .at "
        now we get words like "rat","cat","bat",
     
        if we want words like "@at", or "3at"
     
        r"M[ae][iy]er"  mean first Letter has to be "M"
                           the second letter can be "a" or "e" 
                           the third letter should be "i" or "y"
                           and last two letters must be "er"
     
     
                         __Mai--Maier
              ----Ma---|
        M---|              ---May --Mayer
            |
            |
            |            ---Mei---Meier
             ----Me--|
                        ---Mey--Meyer
     
    r"[a-e][0-5]" -- the first character must be either "a" or "b" or "c" or "d" or "e"
    and second character must be either 0 or 1 or 2 or 3 or 4 or 5
     
    r"[A-Z]"--- first character must b/w uppercase A and Z.
    for if the character can be either upper and lower case alphabet  re"[A-Za-z]"
     
    r"[-ab]"--- the first character can be either "-" or "a" or "b"
    r"[ab-]"-- the first character can be either "-" or "a" or "b"
     
    r"[-a-z]---the first character can be either "-" or any character b/w "a" to "z"
     
    special character caret "^"---negating the choices
    r"[^0-9]" -- any character but a digit
     
    r"[^a-c]" --- anything but an "a","b","c"
     
    r"[a^bc]" --- the first character can be "a", or "^", "b", "c"
     

    """
import re

myDay = "I was born on 27 April 1990"
pattern =r'([\d]{2})[\s]+([A-z]+)[\s]+([\d]+)' 

#compile   Compile a pattern into a RegexObject.
#search    Search a string for the presence of a pattern.

comPat = re.compile(pattern)
birth_day = comPat.search(myDay)
print("The match object",birth_day) #The match object <_sre.SRE_Match object; span=(14, 27), match='27 April 1990'>

print("The complete match",birth_day.group()) #The complete match 27 April 1990
"""
day = birth_day.group(1)  
month = birth_day.group(2)
year = birth_day.group(3) 
"""
day, month, year = birth_day.group()

print(day)    #27
print(month)  #April
print(year)   #1990
#work on find,findall,search,compile,replace,sub

#---re.findall()------
#findall   Find all occurrences of a pattern in a string.

paragraph = """Jude's email-id jude@mail.com,his friend joseph's
            email is joseph@mymail.com.
            """
pattern_email = r'[A-z]+@[A-z]+.[A-z]+'
pattern_name = r'[A-z]+\'s'

email_ids = re.findall(pattern_email,paragraph)
names     = re.findall(pattern_name,paragraph)

print('\n'.join('{}: {}'.format(name,email) for name,email in zip(names,email_ids)))
#Jude's: jude@mail.com
#joseph's: joseph@mymail.com

#---re.split()----
#split     Split a string by the occurrences of a pattern.
pattern_line = r'[;,\s]\s+'
line = 'asdf fjdk; afed, fjek,asdf, foo'
elements = re.split(pattern,line)
print(elements)
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

#capturing the pattern elements
#using groups
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
#['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
#using groups but we dont need the de-limiters
#r'(?:...)
new_fields = re.split(r'(?:,|\;|\s)\s*',line)
print(new_fields)
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

#--- .startswith()----
"""
>>> for method in dir(re):
	if method.startswith('__'):
		print(method)
"""
>>> dunder_files = [ file for file in os.listdir('.') if file.startswith('__') ]
>>> for dunder in dunder_files:
	print(dunder)
		
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
__version__

#--- .startswith()---
>>> import os
>>> os.getcwd()
'C:\\Python34'
>>> #to change the current directory to 'C:\\Python34\Lib\
>>> os.chdir('C:\\\Python34\\Lib\\')
>>> 
>>> os.getcwd()
'C:\\Python34\\Lib'
>>> 
>>> #Listing the folders only
"""
>>> for file in os.listdir('.'):
	if not file.endswith('.py'):
		print(file)
"""
>>> folders = [folder for folder in os.listdir('.') if not file.endswith('.py')]
>>> for folder in folders:
	print(folder)
		
asyncio
collections
concurrent
ctypes
curses
dbm
distutils
email
encodings
ensurepip
html
http
idlelib
importlib
json
lib2to3
logging
msilib
multiprocessing
pydoc_data
site-packages
sqlite3
test
tkinter
turtledemo
unittest
urllib
venv
wsgiref
xml
xmlrpc
__pycache__
>>> 'startswith' in dir(str)
True
>>> 
>>> sentence = "jude work for hcl."
>>> new_job = sentence.replace('hcl','google')
>>> print(new_job)
jude work for google.
>>> info = """james is working in goole.
              james did is MSC in computer science for national university of singapore
              and also a MBA from IIM ahmedabad"""
>>> 
>>> 
>>> info.count('james')
2
>>> new_info = info.replace('james','jude')
>>> new_info
'jude is working in goole.\n              jude did is MSC in computer science for national university of singapore\n              and also a MBA from IIM ahmedabad'
>>> 
#--- .sub() ---
#
