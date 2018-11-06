class Base:
        def __init__(self):
                print "Base class constructor"
        def base_method1(self):
                print "base_method1 method"

class Derived1(Base):
        def __init__(self):
                print "Derived1 class constructor"
        def derived_method1(self):
                print "derived_method1 method"

class Derived2(Derived1):
        def __init__(slef):
                print "Derived2 class constructor"
        def derived2_method1(self): #using derived methods
                print "derived2_method1 method"
                self.derived_method1()
                self.base_method1()

if __name__ == "__main__":
        derived2 = Derived2()
        derived2.derived2_method1()
