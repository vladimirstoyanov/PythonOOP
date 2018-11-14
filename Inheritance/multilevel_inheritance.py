class Base:
        def __init__(self):
                print "Base class constructor"
		self.var1=""
		self.var2=""
        def base_method1(self):
                print "base_method1 method"
	def printVariables(self):
		print "var1: " + str(self.var1)
		print "var2: " + str(self.var2)
		

class Derived1(Base):
        def __init__(self):
                print "Derived1 class constructor"
        def derived_method1(self):
                print "derived_method1 method"

class Derived2(Derived1):
        def __init__(self):
                print "Derived2 class constructor"
		self.var1 = "Derived 2 var1"
		self.var2 = "Derived 2 var2"
        def derived2_method1(self): #using derived methods
                print "derived2_method1 method"
                self.derived_method1()
                self.base_method1()
		self.printVariables()

if __name__ == "__main__":
        derived2 = Derived2()
        derived2.derived2_method1()
