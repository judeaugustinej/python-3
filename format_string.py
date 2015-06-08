"""All about string formating"""

#{} is the placeholder for the substituted variables.

line1 = "My name is {}".format("jude")
print(line1)
#My name is jude


line2 = "{} works for {}".format("jude","HCL")
print(line2)
#jude works for HCL

line3 = "{0} is older than {1}".format("jude","whitson")
print(line3)
#jude is older than whitson

line4 = "{1} is older than {0}".format("jude","whitson")
print(line4)
#'whitson is older than jude'

#Multiple arguments with .format
print("Hi Jude")
print("how are you, can you please introduce yourself")

my_intro ="""
My name is {} ,i am from {} and
i worked with {} for {} years.
Now i work as a {} {} developer.""".format("Jude","bangalore","c-dot",1,"python","openstack")

print(my_intro)
"""--Output---
My name is Jude ,i am from bangalore and
i worked with c-dot for 1 years.
Now i work as a python openstack developer.
"""

#Named Arguments
line5 = "{name} is back".format(name="Jude",)
print(line5)
#Jude is back

#Value consumed multiple times
line6 = "{0},{0} wait !".format("jude")
print(line6)
#jude,jude wait !

################################################
#"Weight in tons {0.weight}"      # 'weight' attribute of first positional arg
#"Units destroyed: {players[0]}"  # First element of keyword argument 'players'.
#"Harold's a clever {0!s}"        # Calls str() on the argument first
#"Bring out the holy {name!r}"    # Calls repr() on the argument first
#"More {!a}"                      # Calls ascii() on the argument first
################################################

class IdCard(object):
  
  def __init__(self,name,_id):
    self.name = name
    self._id = _id
    
  def __str__(self):
    return "This Id-card belong to {0.name} and his sap-id is {0._id}".format(self)
    
  def __repr__(self):
    return "IdCard({0.name},{0._id})".format(self)
    
if __name__ == "__main__":
  
  id1 = IdCard("Jude",5535)
  print(str(id1))  #This Id-card belong to Jude and his sap-id is 5535
  print(repr(id1)) #IdCard(Jude,5535)
  


