class Wallet:
    """Accepts money in rupees
       but store it in dollars
       """
    def __init__(self,rupees):

        self.rupees = rupees

    #Getter Function
    @property
    def rupees(self):
        return self._dollars

    #Setter Function
    @rupees.setter
    def rupees(self,value):
        self._dollars = value * 45

    #Deleter function
    @rupees.deleter
    def rupees(self):

        raise AttributeError("Can't delete attribute")
    
    
if __name__ == "__main__":
    myPurse = Wallet(100)
    print(myPurse.rupees)

    myPurse.rupees = 5
    print(myPurse.rupees)

    oops = [Wallet,myPurse]
    for element in oops:
        for key,value in element.__dict__.items():
            print(str(key)+"-->"+str(value))
        print(" ")
    del myPurse.rupees

#---Output----
"""
>>> 
4500
225
__init__--><function Wallet.__init__ at 0x02D8AF18>
rupees--><property object at 0x030066C0>
__module__-->__main__
__dict__--><attribute '__dict__' of 'Wallet' objects>
__weakref__--><attribute '__weakref__' of 'Wallet' objects>
__doc__-->Accepts money in rupees
       but store it in dollars
       
 
_dollars-->225
 
Traceback (most recent call last):
  File "\\10.166.0.56\chn-project\VDIFoldered\judeaugustine.j\Desktop\python_property\property3.py", line 38, in <module>
    del myPurse.rupees
  File "\\10.166.0.56\chn-project\VDIFoldered\judeaugustine.j\Desktop\python_property\property3.py", line 23, in rupees
    raise AttributeError("Can't delete attribute")
AttributeError: Can't delete attribute
>>> 
"""
