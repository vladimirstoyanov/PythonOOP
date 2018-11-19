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

    def __str__ (self):
        return '{} - {}'.format(self.fullname(), self.email)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employer', 52000)

print (str(emp_1)) #result: Corey Schafer - Corey.Schafer@email.com
print (str(emp_2)) #result: Test Employer - Test.Employer@email.com
