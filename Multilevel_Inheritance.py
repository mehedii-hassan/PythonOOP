class A:
    def display1(self):
        print("This  is A class")


class B(A):
    def display2(self):
        print("This  is B class")


class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("This  is C class")


c = C()
c.display3()
