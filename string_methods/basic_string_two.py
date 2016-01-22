"""
 |  isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |
"""
info = "   I am 25 years old    "
print(info.isalnum()) #True
name = "  jude job\\t"
print(name.isalnum()) #False
"""
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
"""
print(info.isalpha()) #True
age = 25
#print(age.isalpha()) #Raises AttributeError: 'int' object has no attribute 'isalpha'
str_age = '25'
print(str_age.isalpha()) #False
print(name.isalpha()) #True
"""
 |  isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |  
"""
print(str_age.isdigit()) #True
print(name.isdigit())    #False
"""
 |  islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  isspace(...)
 |      S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |  
"""
print(str_age.isspace()) #False
print(name.isspace()) #True
print(name)
# ' \t\n\v\f '.isspace() 
# True
"""
 |  istitle(...)
 |      S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. uppercase characters may only follow uncased
 |      characters and lowercase characters only cased ones. Return False
 |      otherwise.
 |  
 |  isupper(...)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  upper(...)
 |      S.upper() -> string
 |      
 |      Return a copy of the string S converted to uppercase.

"""
