class Whatever:

    def __init__(self,n):
        self.n = n

    @property
    def twice_n(self):

        return self.n * 2

    @twice_n.setter
    def twice_n(self, new_n):

        self.n = new_n / 2

if __name__ == "__main__":

    obj = Whatever(2)
    print(obj.n)#2
    print(obj.twice_n) #4
    obj.twice_n = 10
    print(obj.n) # 5

