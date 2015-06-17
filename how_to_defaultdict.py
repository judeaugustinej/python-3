"""Simple usuage of defaultdict,setdefault"""

#----defaultdict-----
"""
defaultdict is used to create a multi-valued dictionary
Eg.
 d = {
'a' : [1, 2, 3],
'b' : [4, 5]
}
e = {
'a' : {1, 2, 3},
'b' : {4, 5}
}

Now the value can be stored at each value as a list or set.
Use a list if
you want to preserve the insertion order of the items. Use a set if you want to eliminate
duplicates (and don’t care about the order).
"""
>>> from collections import defaultdict
>>>
>>> pairs = [('a',5),('a',67),('b',45),('b',7),('c',3),('d',0)]
>>>
>>>
>>> for key,value in pairs:
...  d[key].append(value)
...
>>> d
defaultdict(<class 'list'>, {'d': [0], 'a': [5, 67], 'c': [3], 'b': [45, 7]})
>>>#let print the key value of dictionary d{}
>>>
>>> for k,v in d.items():
...  print(k,v)
...
d [0]
a [5, 67]
c [3]
b [45, 7]
>>>
>>>#using sets for defaultdict
>>>
>>> dset = defaultdict(set)
>>> dset['a'].add(1)
>>> dset['a'].add(11)
>>> dset['a'].add(111)
>>>
>>> dset['b'].add(2222)
>>>
>>> dset['c'].add(123)
>>> dset['c'].add(321)
>>>
>>> #key value of dset{}
...
>>> for k,v in dset.items():
...  print(k,v)
...
a {1, 11, 111}
c {321, 123}
b {2222}
>>>

#----setdefault----
>>> help(dict.setdefault)
Help on method_descriptor:

setdefault(...)
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

>>> 
>>> pairs = [('a',1),('a',11),('a',111),('b',22),('b',213),('c',232)]
>>> 
>>> for key,value in pairs:
...	dum.setdefault(key,[]).append(value)
>>>
>>>
>>> dum
{'a': [1, 2, 1, 11, 111], 'b': [111, 22, 213], 'c': [232]}
>>>




