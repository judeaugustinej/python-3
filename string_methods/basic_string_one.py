"""
captalize(...)
 |      S.capitalize() -> string
 |      
 |      Return a copy of the string S with only its first character
 |      capitalized.
 |  
"""
name = "jude augustine job"
print(name.capitalize())  
#Jude augustine job
"""
 |  center(...)
 |      S.center(width[, fillchar]) -> string
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
"""
print(name.center(40))
#           jude augustine job           
print(name.center(40,'a'))
#aaaaaaaaaaajude augustine jobaaaaaaaaaaa
note = """
If the string len > width there is now change in the return value.
If the string len < width the return string is paded by default with
empty spaces or by any 'char' if mentioned"""
#print(name.center(40,'abc'))
"""
Traceback (most recent call last):
  File "basic_string.one.py", line 28, in <module>
    print(name.center(40,'abc'))
TypeError: must be char, not str
"""

sentence = """My name is Jude i have 1 year exp\n
in openstack,currently i fix bugs for\n
swift,keystone and unfied openstack client."""
print(sentence.count('i')) #8
print(sentence.count('i',8)) #8
print(sentence.count('i',0,8)) #0
print(sentence.count('i',8,10)) #1
print(sentence.count('openstack')) #2
"""
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are interpreted
 |      as in slice notation.
"""
print(sentence.endswith('client.')) #True
"""
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
"""
print(sentence.find('client.')) #110
print(sentence.endswith('client.',0,110)) #False
print(sentence.endswith('client.',110)) #True
"""
 |      suffix can also be a tuple of strings to try.
 |  find(...)
 |      S.find(sub [,start [,end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
"""
print(sentence.find('HCL')) # -1
#print(sentence.index('cisco')) #Raises ValueError
"""
 |  index(...)
 |      S.index(sub [,start [,end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
"""
