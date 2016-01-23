class A(object):
    def __init__(self):
        print('A.__init__')
        super().__init__()

class B(object):
    def __init__(self):
        print('B.__init__')
        super().__init__()

class C(A, B):
    def __init__(self):
        print('C.__init__')
        super().__init__()

if __name__ == "__main__":
    print(C)
    print(C.mro())
    print(B.mro())
    print(A.mro())
