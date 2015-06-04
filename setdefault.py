#Use case for setdefault method.
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
