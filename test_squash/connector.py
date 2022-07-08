class A:
    a = ""
    def A(self, a):
        self.a = a

class B:
    b = ""
    def B(self, b):
        self.b = b

def add_a_and_b():
    a = A
    b = B
    a.A("a")
    b.B("b")
    return a + b