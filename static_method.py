class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

if __name__ == "__main__":
        obj = MyClass()
        print obj.method()
        print obj.classmethod()
        print obj.staticmethod()
        #print MyClass.method() #error
        print MyClass.classmethod()
        print MyClass.staticmethod()
