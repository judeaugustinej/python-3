class WhatPoint:

    def __init__(self,x,y):
        print("Entering init")
        self.x, self.y = x, y
        print("Exiting init")
        
    def __call__(self,x,y):
        print("Entering call")
        self.x, self.y = x, y
        print("Exiting call")

    def add_distance(self,x,y):
        self.x, self.y = self.x +x ,self.y +y
        return self.x,self.y

    def current_position(self):
        return self.x,self.y

    

        

if __name__ == "__main__":

    a = WhatPoint(6,7)
    print(a.x,a.y)
    
    a(8,9)
    print(a.x,a.y)

    print("An example for method-caller")

    b = WhatPoint(9,9)
    
    from operator import methodcaller
    
    f_current_position = methodcaller('current_position')
    print(f_current_position(b))
    print("----")
    f_add_distance = methodcaller('add_distance',1,2)
    print(f_add_distance(b))
