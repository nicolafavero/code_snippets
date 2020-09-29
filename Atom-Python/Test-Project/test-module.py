

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):

        self.first = first
        self.last = last

        print('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


for num in [1, 2, 3, 4]:
    print(num)

print("dir() Employee: " + str(dir(Employee)))

emp_1 = Employee('John', 'Smith')
