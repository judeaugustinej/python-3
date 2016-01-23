""" Single Inheritance,usecase for ,
    Method Resolution Order(mro).
"""
class A(object):
    def __init__(self):
        print('A.__init__')
        super().__init__()

class B(A):
    def __init__(self):
        print('B.__init__')
        super().__init__()

class C(B):
    def __init__(self):
        print('C.__init__')
        super().__init__()

if __name__ == "__main__":
    print(A.mro())
    print(B.mro())
    print(C.mro()) 

"""
[<class '__main__.A'>, <type 'object'>]
[<class '__main__.B'>, <class '__main__.A'>, <type 'object'>]
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <type 'object'>]
"""

