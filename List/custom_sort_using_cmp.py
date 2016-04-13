# The data
###Not working pls fix it

class Custom(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.name,
                                  self.number)

    def __cmp__(self, other):
        if hasattr(other, 'number'):
            return self.number.__cmp__(other.number)


if __name__ == "__main__":
    customList = [
        Custom('jude', 25),
        Custom('steve', 22),
        Custom('danny', 53)
    ]
    print(customList)
    print(sorted(customList))
    #print(sorted(customList, reverse=True))

