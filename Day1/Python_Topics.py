#x, y, z = input("Enter three values: ").split()
num = [1, 2, 3, 4, 5]

while (n := len(num)) > 0:
    print(num.pop())
x='jayesh'
upper = lambda x: x.upper() 
print(upper(x))

s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))

def starts_a(w):
    return w.startswith("a")

li = ["apple", "banana", "avocado", "cherry", "apricot"]
res = filter(starts_a, li)
print(list(res))

from functools import reduce
def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
res = reduce(add, a)
print(res)
#decorator
#iif args need to add
def decorator(func):
    def wrapper(*args):
        print("Before calling the function.")
        func(*args)
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet(s):
    print("Hello, World!" + s)
greet('jayesh')

name = "Alice"
age = 22
#using f string
print(f"Name: {name}, Age: {age}")
#using format
print("Name: {}, Age: {}".format(name,age))


tup = (1, 2, 3, 4, 5)
#* used to unpack multiple values
a, *b, c = tup
print(b)

from collections import OrderedDict

od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3

print(list(od.items()))

# Step 1: Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'
    
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Fedrick", 50000)
print(emp.name)       
print(emp.__salary)

class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")