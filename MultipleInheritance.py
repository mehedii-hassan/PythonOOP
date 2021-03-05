class A:
    def display(self):
        print("This  is A class")


class B:
    def display(self):
        print("This  is B class")


class C(A, B):
    def display3(self):
        print("This  is C class")


c = C()
c.display3()
