class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a + other

print(A(1) + 2)