class Parent(object):
        def __init__ (self):
                self.value = 5

        def get_value(self):
                return self.value


class Child(Parent):
        def get_value(self):
                return self.value + 1


if __name__ == "__main__":
        c = Child()
        print c.get_value()
