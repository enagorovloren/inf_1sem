class A:
    def method(self):
        print('method A')

class B(A):
    def method(self):
        super().method()
        print('method B')

b = B()
b.method()