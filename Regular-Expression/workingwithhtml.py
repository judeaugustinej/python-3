#Parsing html file using re module

"""
>>> import re
>>> pattern = r'May|Jude'
>>> re.search(pattern,'where is May')
<_sre.SRE_Match object; span=(9, 12), match='May'>
>>> 
>>> 
>>> re.search(pattern,'where is Jude')
<_sre.SRE_Match object; span=(9, 13), match='Jude'>
>>> 
>>> 
>>> re.findall(pattern,'how is Jude.May is very hot')
['Jude', 'May']
>>> 
"""
import re
