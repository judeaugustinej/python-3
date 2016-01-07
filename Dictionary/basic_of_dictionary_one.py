 #Example for variour dictionary methods
 
 """
  items(...)
     D.items() -> a set-like object providing a view on D's items
     
  values(...)
      D.values() -> an object providing a view on D's values
 
 
  keys(...)
     D.keys() -> a set-like object providing a view on D's keys
 """
>>> d = {'hcl':'mymail','goole':'gmail','yahoo':'ymail'}
>>> 
>>> for key,value in d.items():
...	print(key,value)
yahoo ymail
hcl mymail
goole gmail
>>>
>>> d.values()
dict_values(['ymail', 'mymail', 'gmail'])
>>> 
>>> d.keys()
dict_keys(['yahoo', 'hcl', 'goole'])
>>> 
>>> d.items()
dict_items([('yahoo', 'ymail'), ('hcl', 'mymail'), ('goole', 'gmail')])
>>>
>>> 




 """
  get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 
clear(...)
     D.clear() -> None.  Remove all items from D.
 
 copy(...)
     D.copy() -> a shallow copy of D
 
 fromkeys(iterable, value=None, /) from builtins.type
     Returns a new dict with keys from iterable and values equal to value.


 pop(...)
     D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
      If key is not found, d is returned if given, otherwise KeyError is raised

  popitem(...)
     D.popitem() -> (k, v), remove and return some (key, value) pair as a
     2-tuple; but raise KeyError if D is empty.
 

 update(...)
     D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
     If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
     If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
     In either case, this is followed by: for k in F:  D[k] = F[k]
 


 """
