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
        #result:
        #('instance method called', <__main__.MyClass instance at 0xb71d2b0c>)
        #('class method called', <class __main__.MyClass at 0xb71d708c>)
        #static method called
        #('class method called', <class __main__.MyClass at 0xb71d708c>)
        #static method called

