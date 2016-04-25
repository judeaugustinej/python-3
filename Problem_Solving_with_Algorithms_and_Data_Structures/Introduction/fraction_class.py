def gcd(m, n):
    while m%n !=0:
        oldm = m
        oldn = n
        
        m = oldn
        n = oldm%oldn
    return n


class Fraction(object):

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        n = gcd(new_num, new_den)
        return Fraction(new_num//n, new_den//n)

    def __eq__(self, other):
        firstnum = self.num* other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        n = gcd(new_num, new_den)
        return Fraction(new_num//n, new_den//n)

    def __mul__(self, other):
        pass
    
if __name__ == "__main__":
    x1 = Fraction(4, 11)
    x2 = Fraction(5, 11)
    print(x2.den, x2.num, x1.den, x1.num)
    print(x1+x2) 
    print(x1 == x2)
    print(x1-x2)
    print(x2-x1)
