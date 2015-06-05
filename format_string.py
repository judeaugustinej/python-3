"""All about string formating"""

#{} is the placeholder for the substituted variables.

print("My name is {}".format("jude"))
#My name is jude

line = "My name is {}".format("jude")
print(line)
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
