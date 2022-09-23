# Inheritance versus Composition
# Inheritance
# implicit override alter
class Parent(object):
    def Implicit(self):
        print("父类 调用Implicit")


class Child(Parent):
    def Implicit(self):
        print("子类 alter之前")
        super(Child, self).Implicit()
        print("子类 alter之后")


dad = Parent()
son = Child()

dad.Implicit()
son.Implicit()


# Composition
class Other(object):
    def override(self):
        print("Other override")

    def implicit(self):
        print("Other implicit")

    def altered(self):
        print("Other altered")


class Compos(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Compos override")

    def altered(self):
        print("before, altered")
        self.other.altered()
        print("after, altered")


compos = Compos()
compos.implicit()
compos.override()
compos.altered()
