class Base1:
        def __init__(self):
                print "Base1 class constructor"
                pass

        def base1_method1 (self):
                print "base1_method1 method"


class Base2:
        def __init__(self):
                print "Base2 class constructor"
                pass

        def base2_method2(self):
                print "base2_method2 method"


class MultiDerived(Base1, Base2):
        def __init__(self):
                print "MultiDerived class constructor"
                pass
        def multiderived_method1(self):
                print "multiderived_method1 method"
                self.base1_method1()
                self.base2_method2()



if __name__ == "__main__":
        multi = MultiDerived()
        multi.multiderived_method1()
