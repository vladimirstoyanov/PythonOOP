class Employee:

    raise_amt = 1.04

    def __init__  (self, first, last, pay):
        self.first = first
        self. last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname (self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise (self):
        self.pay = int(self.pay + self.raise_amt)

    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employer', 52000)

print(emp_1 + emp_2) #result: 102000
