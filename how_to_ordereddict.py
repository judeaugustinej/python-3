"""Simple usuage of ordereddict.
An OrderedDict can be particularly useful when you want to build a mapping that you
may want to later serialize or encode into a different format.
"""
>>> from collections import OrderedDict
>>> 
>>> d ={}
>>> d = OrderedDict()
>>> type(d)
<class 'collections.OrderedDict'>
>>> 
>>> d['jude'] = 'job'
>>> d['james'] = 'daniel'
>>> d['john'] = 'joseph'
>>> 
>>> d
OrderedDict([('jude', 'job'), ('james', 'daniel'), ('john', 'joseph')])
>>> 
>>> for k,v in d.items():
	print(k,v)

	
jude job
james daniel
john joseph
>>> 
