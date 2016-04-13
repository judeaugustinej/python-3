class Custom(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.name,
                                  self.number)

def getKey(custom):
    return custom.number

if __name__ == "__main__":
    customList = [
        Custom('jude', 25),
        Custom('steve', 22),
        Custom('danny', 53)
    ]
    print(sorted(customList, key=getKey))
    print(sorted(customList, key=getKey, reverse=True))
