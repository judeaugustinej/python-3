#Use case for setdefault method.
#If check for key,value in data.
#If key is found we append the value,else we add new key-value pair.
#Example ---1
# really verbose
new = {}
for (key, value) in data:
    if key in new.keys():
        new[key].append( value )
    else:
        new[key] = [value]


# easy with setdefault
"""
 setdefault(...)
     D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 
"""
new = {}
for (key, value) in data:
    group = new.setdefault(key, []) # key might exist already
    group.append( value )


# even simpler with defaultdict 
new = defaultdict(list)
for (key, value) in data:
    new[key].append( value ) # all keys have a default already

#Example ---2
"""
d = {}
# To add a key->value pair, do the following:
d.setdefault(key, []).append(value)

# To retrieve a list of the values for a key
list_of_values = d[key]

# To remove a key->value pair is still easy, if
# you don't mind leaving empty lists behind when
# the last value for a given key is removed:
d[key].remove(value)

# Despite the empty lists, it's still possible to 
# test for the existance of values easily:
if d.has_key(key) and d[key]:
    pass # d has some values for key

# Note: Each value can exist multiple times!
"""
e = {}
print(e)
e.setdefault('Cars', []).append('Toyota')
print(e)
e.setdefault('Motorcycles', []).append('Yamaha')
print(e)
e.setdefault('Airplanes', []).append('Boeing')
print(e)
e.setdefault('Cars', []).append('Honda')
print(e)
e.setdefault('Cars', []).append('BMW')
print(e)
e.setdefault('Cars', []).append('Toyota')
print(e)

# NOTE: now e['Cars'] == ['Toyota', 'Honda', 'BMW', 'Toyota']
e['Cars'].remove('Toyota')
print(e)
# NOTE: it's still true that ('Toyota' in e['Cars'])
#If the key is not found in the dictionary,
#we add the key to the dictionary assign a default value
#In the below example it is an empty list
#With-out setdefault
dict_ = {}

if "one" not in dict_:
   #If the key "one" is not found in the dictionary dict_
   #it is creted and given a value of an empty list
   dict_["one"] = []
  
  
   print(dict_)

#--Output---
# {'one': []}

#If the key is not found we add it to the dictionary,
#key is given a default value of an empty list
#Using setdefault

dictionary = {}

if "two" not in dictionary:

   dictionary.setdefault("key",[])
   
print(dictionary)

#--Output--
#{'key': []}


